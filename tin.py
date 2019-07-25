#!/usr/bin/env python3
import time
print()
'''
per = '0% >'
for i in range(10):
    pera = per.index(">")
    per = per[:pera] + "==" + per[pera:] 
    
    print(f'{i}{per}', end="\r")
    time.sleep(1)
print("100% ====================||| \n         DONE!")
'''

per = '%  >'
for i in range(100):
    pera = per.index(">")
    if i % 2 == 0 or i == 0:
        per = per[:pera] + "-" + per[pera:]
    print(f'{i}{per}', end='\r')
    time.sleep(.05)
print("100%")

