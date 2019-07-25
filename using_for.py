#!/usr/bin/env python3

pets = [{"cat": "small"}, {"dog":"medium"}, {"hamster": "tiny"}, {"koala": "medium"}, {"goat": "medium"}, {"snake": "small"}, {"bison": "large"}]

a = iter(pets)
print(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
'''

tiny = []
small = []
medium = []
large = []

for pet in pets:
    # Does the value match?
    # print(pet.items())
    # dict_items([('cat', 'small')])
    
    for key, value in pet.items():
        if value == "tiny":
            tiny.append(key)
        elif value == "small":
            small.append(key)
        elif value == "medium":
            medium.append(key)
        else:
            large.append(key)

print("tiny", tiny)
print("small", small)
print("medium", medium)
print("large", large)
'''
'''
servers = [{"IP": "10.10.22.22"}, {"IP": "10.22.22.44"}]

for addr in servers:
    print(addr["IP"])
'''
'''
for pet in pets:
    print(pet)
    if pet == "dog":
        print(f"{pet}s rule!")
'''


'''

nums = [1, 7, 22, 13, 64, 509]
for num in nums:
    print(num)
    if num < 10:
        print("little")
    elif num < 50:
        print("medium")
    elif num < 100:
        print("large")
    else:
        print("number out of range")

print("All done!")
'''

