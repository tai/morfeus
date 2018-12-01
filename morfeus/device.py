#!/usr/bin/env python3
"""
Library to control moRFeus mixer/signal generator.

Usage:
  import morfeus

  mrf = morfeus.MoRFeus()
  mrf.mode = morfeus.Mode.GENERATOR
  mrf.frequency = 120000000

"""

import hid
import enum
from struct import pack, unpack

VID = 0x10C4
PID = 0xEAC9

CMD_GET = 0x72
CMD_SET = 0x77

class Mode(enum.Enum):
    MIXER = 0
    GENERATOR = 1

class MoRFeus(object):
    """Creates instance to control moRFeus.

Example:
  mrf = MoRFeus()
  mrf = MoRFeus(morfeus.VID, morfeus.PID)
"""
    def __init__(self, vid=VID, pid=PID, index=0):
        try:
            found = hid.enumerate(VID, PID)[index]
            self.dev = hid.device()
            self.dev.open_path(found['path'])
        except IndexError as e:
            raise Exception("No device found") from e

    @property
    def freq(self):
        """Get or set Frequency in HZ
Example:
  mrf.freq = 120000000
  print(mrf.freq)
"""
        dev = self.dev
        msg = pack(">BB14x", CMD_GET, 0x81)
        dev.write(msg)

        ret = dev.read(16)
        return int.from_bytes(ret[2:10], byteorder='big', signed=False)

    @freq.setter
    def freq(self, freq):
        dev = self.dev
        msg = pack(">BBQ6x", CMD_SET, 0x81, freq)
        dev.write(msg)
        dev.read(16)

    @property
    def mode(self):
        """Get or set function mode
Example:
  mrf.mode = morfeus.Mode.MIXER
  print(mrf.mode)
  mrf.mode = morfeus.Mode.GENERATOR
  print(mrf.mode)
"""
        dev = self.dev
        msg = pack(">BB14x", CMD_GET, 0x82)
        dev.write(msg)

        ret = dev.read(16)
        val = int.from_bytes(ret[2:10], byteorder='big', signed=False)
        return Mode(val)

    @mode.setter
    def mode(self, mode):
        dev = self.dev
        msg = pack(">BBQ6x", CMD_SET, 0x82, mode.value)
        dev.write(msg)
        dev.read(16)

    @property
    def current(self):
        """Get or set current level
Example:
  mrf.current = 1
  print(mrf.current)
"""
        dev = self.dev
        msg = pack(">BB14x", CMD_GET, 0x83)
        dev.write(msg)

        ret = dev.read(16)
        return int.from_bytes(ret[2:10], byteorder='big', signed=False)

    @current.setter
    def current(self, level=0):
        dev = self.dev
        msg = pack(">BBQ6x", CMD_SET, 0x83, level)
        dev.write(msg)
        dev.read(16)

    @property
    def bias(self):
        """Get or set Bias-T status
Example:
  mrf.bias = 1
  print(mrf.bias)
"""
        dev = self.dev
        msg = pack(">BB14x", CMD_GET, 0x84)
        dev.write(msg)

        ret = dev.read(16)
        return int.from_bytes(ret[2:10], byteorder='big', signed=False)

    @bias.setter
    def bias(self, status=0):
        dev = self.dev
        msg = pack(">BBQ6x", CMD_SET, 0x84, status)
        dev.write(msg)
        dev.read(16)

if __name__ == '__main__' and '__file__' in globals():
    from IPython import embed
    mrf = MoRFeus()
    embed()
