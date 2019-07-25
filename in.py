#!/usr/bin/env python3
import pdb


my_text = "I want to ride a donkey down the Grand Canyon trails"
count = 0
pdb.set_trace()
if "an" in my_text:
    print("There is an 'an' in your text")

for letter in my_text:
    if "a" == letter:
        count += 1

print(count)
