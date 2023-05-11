#!/usr/bin/python3
if __name__ = "__main__":
    from sys import argv
    arg_sum = 0
    for n in range(len(argv) - 1):
        arg_sum += (int(argv[n + 1]))
        print("{:d}".format(arg_sum))
