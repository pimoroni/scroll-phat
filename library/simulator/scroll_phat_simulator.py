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
LED_SIZE_PX = 50
LINE_WIDTH_PX = 5

WINDOW_HEIGHT_PX = LED_SIZE_PX * ROWS + LINE_WIDTH_PX * (ROWS - 1)
WINDOW_WIDTH_PX = LED_SIZE_PX * COLUMNS + LINE_WIDTH_PX * (COLUMNS - 1)

DRAW_TIMEOUT_MS = 100


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

    def running(self):
        raise NotImplementedError()

    def destroy(self):
        raise NotImplementedError()


class TkPhatSimulator(ScrollPhatSimulator):
    def __init__(self):
        self.brightness = 70
        self.do_run = True
        self.pixels = [[False]*ROWS for i in range(COLUMNS)]

        self.root = tk.Tk()
        self.root.resizable(False, False)

        self.root.bind('<Control-c>', lambda _: self.destroy())
        self.root.bind("<Unmap>", lambda _: self.destroy())
        self.root.protocol('WM_DELETE_WINDOW', self.destroy)

        self.root.title('scroll pHAT simulator')
        self.root.geometry('{}x{}'.format(WINDOW_WIDTH_PX, WINDOW_HEIGHT_PX))
        self.canvas = tk.Canvas(
            self.root, width=WINDOW_WIDTH_PX, height=WINDOW_HEIGHT_PX)
        self.canvas.config(highlightthickness=0)

    def run(self):
        try:
            self.draw_pixels()
            self.root.mainloop()
        except Exception as e:
            print(e)
            self.destroy()

    def destroy(self):
        self.do_run = False

    def running(self):
        return self.do_run

    def draw_pixels(self):
        if not self.running():
            self.root.destroy()
            return

        self.canvas.delete(tk.ALL)
        self.canvas.create_rectangle(
            0, 0, WINDOW_WIDTH_PX, WINDOW_HEIGHT_PX, width=0, fill='black')

        color = '#%02x%02x%02x' % (
            self.brightness, self.brightness, self.brightness)

        for col in range(COLUMNS):
            for row in range(ROWS):
                x = (LED_SIZE_PX + LINE_WIDTH_PX) * col
                y = (LED_SIZE_PX + LINE_WIDTH_PX) * row
                self.canvas.create_rectangle(x, y, x + LED_SIZE_PX, y + LED_SIZE_PX, width=0, fill=color
                                             if self.pixels[col][row] else 'black')

        self.canvas.pack()

        self.root.after(DRAW_TIMEOUT_MS, self.draw_pixels)

    def set_pixels(self, vals):
        for col in range(COLUMNS):
            for row in range(ROWS):
                self.pixels[col][row] = vals[col] & (1 << row)

    def set_brightness(self, brightness):
        # the scroll phat has a pretty high minimum brightness, even at 1 it is quite visible
        # and most examples seem to set it in the range 3..20, so we want to make those changes
        # quite noticeable, with decreasing difference as we go higher in the band

        self.brightness = 100 + int(brightness*155/255)


class ReadThread:
    def __init__(self, scroll_phat_simulator):
        self.scroll_phat_simulator = scroll_phat_simulator
        self.stdin_thread = threading.Thread(
            target=self._read_stdin, daemon=True)

    def start(self):
        self.stdin_thread.start()

    def join(self):
        self.stdin_thread.join()

    def _read_stdin(self):
        while self.scroll_phat_simulator.running():
            try:
                self._handle_command(pickle.load(sys.stdin.buffer))
            except EOFError:
                self.scroll_phat_simulator.destroy()
            except Exception as err:
                print(err)
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

    signal.signal(signal.SIGINT, lambda sig, frame: sys.exit(0))

    phat = TkPhatSimulator()
    thread = ReadThread(phat)
    thread.start()
    phat.run()
    thread.join()


if __name__ == "__main__":
    main()
