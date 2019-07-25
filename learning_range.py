#!/usr/bin/env python3
'''
for item in range(133, 142):
    print(item)

print(item + 1)
'''
# Opening files
import pprint
# Old way
sfile = open("using_for.py", "r")
lines = sfile.readlines()
for row in lines:
    print(row, end=" ")
sfile.close()

# New Way
with open("astros.py", "w") as spacefile:
    spacefile.write("Astronauts are cool!")


