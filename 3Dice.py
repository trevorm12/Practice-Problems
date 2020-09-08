# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 17:04:27 2020

@author: trevm
"""

import random

dieSides = [1, 2, 3, 4, 5, 6]

dieOne = random.choice(dieSides)
dieTwo = random.choice(dieSides)
dieThree = random.choice(dieSides)

print("First Die: " + str(dieOne))
print("Second Die: " + str(dieTwo))
print("Third Die:" + str(dieThree))