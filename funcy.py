#!/usr/bin/env python3

p = 7
a = p
p += 1
print(a)


d = {"key": "value"}
e = d.copy()
d["key2"] = "value2"
print(d, e)

f = ['cat']
g = f.copy()
f.append('dog')
print(f, g)

def do_math(x, y):
    x = x + y
    return x

do_math(p, 12)


