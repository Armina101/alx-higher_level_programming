#!/usr/bin/python3
if __name__ = "__main__":
    from sys import argv
    num = len(argv) - 1
    if num == 0:
        print(0)
    else:
        arg_sum = 0
        for n in range(1, num + 1):
            arg_sum += (int(argv[n]))
            print(arg_sum)
