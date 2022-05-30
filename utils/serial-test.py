#!/usr/bin/env python3

"""Flood serial bridge to test app strength."""

import time
import string
import random
import secrets
import serial

# some const
BUNDLE = string.ascii_letters + string.digits


# some functions
def msg_crc16(msg: bytes) -> int:
    """Compute CRC16 of a bytes message."""
    crc = 0xFFFF
    for item in msg:
        next_byte = item
        crc ^= next_byte
        for _ in range(8):
            lsb = crc & 1
            crc >>= 1
            if lsb:
                crc ^= 0xA001
    return crc


if __name__ == '__main__':
    sp = serial.Serial(port='/dev/ttyUSB0', baudrate=921600)

    while True:
        # publish a random string and test value in DB
        rand_str = ''.join(secrets.choice(BUNDLE) for i in range(random.randint(8, 64)))
        frame = f'{{"type":"rkey", "key":"test", "val": "{rand_str}"}}'.encode()
        frame_crc = msg_crc16(frame)
        frame = frame + f'{frame_crc:04X}\n'.encode()
        sp.write(frame)
        time.sleep(1.0)
