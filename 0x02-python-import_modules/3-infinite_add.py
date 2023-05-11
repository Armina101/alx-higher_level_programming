#!/usr/bin/python3
if __name__ = "__main__":
    import sys
    arg_sum = 0
    for n in range(len(sys.argv) - 1):
        arg_sum += (int(sys.argv[i + 1]))
        print("{:d}".format(arg_sum))
