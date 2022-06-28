#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(65 + ord(c) - 97)
            new_str = new_str + c
        elif ord(c) >= 65 and ord(c) <= 90:
            new_str = new_str + c
        elif ord(c) == 32:
            new_str=new_str + " "
        else:
            new_str = new_str + c
    print("{:s}".format(new_str))
