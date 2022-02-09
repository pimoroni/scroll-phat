import sys
import subprocess
from collections import namedtuple
import pickle
import os
from scroll_phat_simulator import Cmds

Command = namedtuple('Command', ['cmd', 'vals'])


class SMBus:
    def __init__(self, dummy):
        self._start_simulator()

    def _start_simulator(self):
        self.sdl_phat_process = subprocess.Popen(
            [sys.executable, os.path.dirname(os.path.abspath(
                __file__)) + '/scroll_phat_simulator.py'],
            stdin=subprocess.PIPE)

    def write_i2c_block_data(self, addr, cmd, vals):
        I2C_ADDR = 0x60
        MODE_5X11 = 0b00000011

        assert addr == I2C_ADDR

        parsed_cmd = Cmds(cmd)

        if parsed_cmd == Cmds.CMD_SET_MODE:
            assert len(vals) == 1
            assert vals[0] == MODE_5X11
        elif parsed_cmd == Cmds.CMD_SET_BRIGHTNESS:
            assert len(vals) == 1
        elif parsed_cmd == Cmds.CMD_SET_PIXELS:
            assert len(vals) == 12
            assert vals[-1] == 0xFF

        try:
            pickle.dump(Command(cmd=parsed_cmd, vals=vals),
                        self.sdl_phat_process.stdin)
            self.sdl_phat_process.stdin.flush()
        except OSError:
            print('lost connection with scroll pHAT simulator')
            sys.exit(-1)
