#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n_args = len(sys.argv)

    if n_args == 2:
        print("1 argument:".format(n_args - 1))
        print("1: {:s}".format(sys.argv[1]))

    elif n_args > 2:
        print("{:d} arguments:".format(n_args - 1))
        counter = 1
        while counter < n_args:
            print("{:d}: {:s}".format(i, sys.argv[i]))
            counter += 1
    else:
        print("0 arguments.")
