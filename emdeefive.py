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
except (EOFError, KeyboardInterrupt):
    pass
