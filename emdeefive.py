#!/usr/bin/env python3
# Convert an input list of passwords into an output list of hashes.
# Use like "python emdeefive.py | tee hashes.txt" or "python emdeefive.py < password.txt > hashes.txt"
import hashlib

try:
    while True:
        password = input("")

        m = hashlib.md5()
        m.update(password.encode())
        hash = m.digest().hex()

        print(hash)

        if hash == 'fc8767a5e9e2382a17072b10725e1c8b':
            print('You win!')
            break
except (EOFError, KeyboardInterrupt):
    pass
