import threading
import sys
import errno
import pickle
import tkinter as tk
from enum import Enum
import time
import signal

ROWS = 5
COLUMNS = 11
PIXELS_PER_LED = 50
LINE_WIDTH = 5

WINDOW_HEIGHT = PIXELS_PER_LED * ROWS + LINE_WIDTH * (ROWS - 1)
WINDOW_WIDTH = PIXELS_PER_LED * COLUMNS + LINE_WIDTH * (COLUMNS - 1)


class Cmds(Enum):
    CMD_SET_MODE = 0x00
    CMD_SET_BRIGHTNESS = 0x19
    CMD_SET_PIXELS = 0x01


class ScrollPhatSimulator:
    def set_pixels(self, vals):
        raise NotImplementedError()

    def set_brightness(self, brightness):
        raise NotImplementedError()

    def run(self):
        raise NotImplementedError()

    def destroy(self):
        raise NotImplementedError()


class TkPhatSimulator(ScrollPhatSimulator):
    def __init__(self):
        self.brightness = 70
        self.running = True
        self.pixels = [[False]*ROWS for i in range(COLUMNS)]

        self.root = tk.Tk()
        self.root.resizable(False, False)

        self.root.bind('<Control-c>', lambda _: self.destroy())
        self.root.bind("<Unmap>", lambda _: self.destroy())
        self.root.protocol('WM_DELETE_WINDOW', self.destroy)

        self.root.title('scroll pHAT simulator')
        self.root.geometry('{}x{}'.format(WINDOW_WIDTH, WINDOW_HEIGHT))
        self.canvas = tk.Canvas(
            self.root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.canvas.config(highlightthickness=0)

    def run(self):
        try:
            self.draw_pixels()
            self.root.mainloop()
        except Exception as e:
            print(e)
            self.destroy()

    def destroy(self):
        self.running = False

    def draw_pixels(self):
        if not self.running:
            self.root.destroy()
            return

        self.canvas.delete(tk.ALL)
        self.canvas.create_rectangle(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, width=0, fill='black')

        color = '#%02x%02x%02x' % (self.brightness, self.brightness, self.brightness)

        for col in range(COLUMNS):
            for row in range(ROWS):
                x = (PIXELS_PER_LED + LINE_WIDTH) * col
                y = (PIXELS_PER_LED + LINE_WIDTH) * row
                self.canvas.create_rectangle(x, y, x + PIXELS_PER_LED, y + PIXELS_PER_LED, width=0, fill=color
                                             if self.pixels[col][row] else 'black')

        self.canvas.pack()

        self.root.after(100, self.draw_pixels)

    def set_pixels(self, vals):
        for col in range(COLUMNS):
            for row in range(ROWS):
                self.pixels[col][row] = vals[col] & (1 << row)

    def set_brightness(self, brightness):
        # the scroll phat has a pretty high minimum brightness, even at 1 it is quite visible
        # and most examples seem to set it in the range 3..20, so we want to make those changes
        # quite noticeable, with decreasing difference as we go higher in the band

        self.brightness = 100 + int(brightness*155/255)


class FifoThead:
    def __init__(self, fifo_name, scroll_phat_simulator):
        self.fifo_name = fifo_name
        self.scroll_phat_simulator = scroll_phat_simulator

        self.fifo = None
        self.fifo_thread = threading.Thread(target=self._read_fifo, daemon=True)

    def start(self):
        self.fifo_thread.start()

    def _read_fifo(self):
        while True:
            try:
                if not self.fifo:
                    self.fifo = open(self.fifo_name, 'rb')
                self._handle_command(pickle.load(self.fifo))
            except FileNotFoundError:
                print('waiting for fifo', self.fifo_name)
                time.sleep(1)
            except OSError as err:
                if err.errno not in [errno.EAGAIN, errno.EWOULDBLOCK]:
                    raise
                print(err)
            except Exception:
                self.scroll_phat_simulator.destroy()

    def _handle_command(self, command):
        # for some reason i need to compare the values here, perhaps a pickling issue?
        if command.cmd.value == Cmds.CMD_SET_BRIGHTNESS.value:
            assert len(command.vals) == 1
            self.scroll_phat_simulator.set_brightness(command.vals[0])
        elif command.cmd.value == Cmds.CMD_SET_PIXELS.value:
            assert len(command.vals) == 12
            assert command.vals[-1] == 0xFF
            self.scroll_phat_simulator.set_pixels(command.vals)


def main():
    print('starting scroll pHAT simulator')

    if len(sys.argv) != 2:
        print('need to specify fifo name')
        sys.exit(1)

    fifo_name = sys.argv[1]

    signal.signal(signal.SIGINT, lambda sig, frame: sys.exit(0))

    phat = TkPhatSimulator()
    thread = FifoThead(fifo_name, phat)
    thread.start()
    phat.run()


if __name__ == "__main__":
    main()
