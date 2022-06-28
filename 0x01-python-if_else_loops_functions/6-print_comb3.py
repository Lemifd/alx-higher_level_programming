#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if j > i and i < 8:
            print(f"{i}{j}, ", end="")
        elif j > i and i >= 8:
            print(f"{i}{j}", end="\n")
