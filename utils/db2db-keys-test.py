#!/usr/bin/env python3

"""Test data transmit of random strings between bridges nodes.

node0 (on redis db 0) -> node1 (on redis db 1)
 tx:node1:test-UUID       rx:node0:test-UUID

use USB Null Modem Cable between /dev/ttyUSB0 and /dev/ttyUSB1
on node0: ./redis-serial-sync --remote node1 --db 0 /dev/ttyUSB0
on node1: ./redis-serial-sync --remote node0 --db 1 /dev/ttyUSB1
"""

import atexit
import time
import string
import random
import secrets
import uuid
import redis

# some const
CHARS_BUNDLE = string.ascii_letters + string.digits + string.punctuation


if __name__ == '__main__':
    db0 = redis.StrictRedis(db=0)
    db1 = redis.StrictRedis(db=1)
    key_uuid = uuid.uuid4()
    tx_key = f'tx:node1:test-{key_uuid}'
    rx_key = f'rx:node0:test-{key_uuid}'
    good_count = 0

    def on_exit():
        """Exit handler."""
        # time to processing last request before clean
        time.sleep(.5)
        # clean db1 at exit
        db1.delete(rx_key)
    atexit.register(on_exit)

    while True:
        # get a random string from bundle char src
        rand_str = ''.join(secrets.choice(CHARS_BUNDLE) for i in range(random.randint(64, 4096)))
        # send tx random bytes
        tx_rand_bytes = rand_str.encode()
        db0.set(tx_key, tx_rand_bytes)
        # wait for transmit node0 -> serial -> node1
        time.sleep(1.0)
        # receive rx random bytes
        rx_rand_bytes = db1.get(rx_key)
        # print test result
        if rx_rand_bytes != tx_rand_bytes:
            print('-' * 80)
            print('MISMATCH DETECT')
            print(f'{tx_key} is {tx_rand_bytes}')
            print(f'{rx_key} is {rx_rand_bytes}')
            good_count = 0
        else:
            if not good_count % 80:
                print('')
            print('.', end='', flush=True)
            good_count += 1
