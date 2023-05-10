#!/usr/bin/python3
for a in range(0, 10):
    for b in range(a + 1, 10):
        print("{:d}{:d}".format(x, y), end=" ")
        if a != 8 or b != 9:
            print(",", end=" ")
            print()
