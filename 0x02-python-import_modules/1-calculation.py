#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    print("{:d} + {:d} = {:d}".format(10, 5, add(10, 5)))
    print("{:d} - {:d} = {:d}".format(10, 5, sub(10, 5)))
    print("{:d} * {:d} = {:d}".format(10, 5, mul(10, 5)))
    print("{:d} / {:d} = {:d}".format(10, 5, div(10, 5)))
