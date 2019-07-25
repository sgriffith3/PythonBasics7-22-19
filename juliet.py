#!/usr/bin/env python3

j_count_speaking = 0
j_count = 0

with open("romeo.txt") as play:
    lines = play.readlines()
    for name in lines:
        if "JULIET" == name.strip():
            j_count_speaking += 1  # j_count_speaking = j_count_speaking + 1
        if "juliet" in name.lower():
            j_count += 1

print(j_count_speaking)
print(j_count)


