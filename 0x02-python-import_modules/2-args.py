#!/usr/bin/python3
import sys
if len(sys.argv) - 1 > 1:
    print("{:d} arguments:".format(len(sys.argv) - 1))
elif len(sys.argv) - 1 == 0:
    print("{:d} arguments.".format(0))
else:
    print("{:d} argument:".format(1))
for i in range(1, len(sys.argv)):
    print("{:d}: {:s}".format(i, sys.argv[i]))
