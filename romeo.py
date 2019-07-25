#!/usr/bin/env python3

count = 0
with open("romeo.txt") as romeo:
    text = romeo.readlines()
    for line in text:
        if "ROMEO" in line:
            count += 1

print(count)
