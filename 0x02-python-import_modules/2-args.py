#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = len(argv) - 1

    if num == 0:
        print("0 arguments.")
    elif num == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num))
        for a in range(num):
            print("{}: {}".format(a + 1, argv[a + 1]))
