#!/usr/bin/env python3

def mathy(x, y):
    answer = x + y
    return answer

def subby(a):
    less_than = 100 - a
    print(less_than)


#the_sum = mathy(10, 15)
#subby(the_sum)
subby(mathy(10, 15))

def fancy(k, l, m):
    plus = k + l + m
    minus = k - l - m
    return plus, minus

print(fancy(12, 34, 56))

first, second = fancy(12, 34, 56)
print(mathy(first, second))

print(mathy(*fancy(12,34,56)))

