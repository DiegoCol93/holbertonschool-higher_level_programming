#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    ac = len(argv)

    if ac == 4:
        if argv[2] == '+':
            print(add(int(argv[1]), int(argv[3])))
        elif argv[2] == '-':
            print(sub(int(argv[1]), int(argv[3])))
        elif argv[2] == '*':
            print(mul(int(argv[1]), int(argv[3])))
        elif argv[2] == '/':
            print(div(int(argv[1]), int(argv[3])))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
