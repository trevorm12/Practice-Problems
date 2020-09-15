# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import math

#Question 1
print()
print("Question 1:")
print(np.sqrt(23))

#Question 2
print()
print("Question 2")
print(math.sin(math.pi / 2))

#Question 3
print()
print("Question 3")
radius = 2.3
volume = (4/3) * math.pi * radius
print(volume)

#Question 4
print()
print("Question 4")
totalTime = 234513.6
numHours = math.floor(totalTime / 3600)
print("Hours: " + str(numHours))
numMins = math.floor(totalTime / 60)
print("Mins: " + str(numMins))
numSecs = math.floor(totalTime)
print("Secs: " + str(numSecs))

#Question 5
print()
print("Question 5")
exec(open('3Dice.py').read())

#Question 6
print()
print("Question 6: ")
loanAmount = input("Please enter the loan amount: ")
numberOfYears = input("Please enter the number of years: ")
monthlyInterestRate = input("Please enter the monthly interest rate: ")
monthlyPayment = loanAmount*(1+monthlyInterestRate)^(numberOfYears*12)
print(monthlyPayment)

#Question 7
print()
print("Question 7: ")
tempF = input("Please enter a temperature in Farenheit: ")
tempC = (tempF - 32) * (5/9)
print(tempC)

#Question 8
print()
print("Question 8: ")
timeDiff = input("How many timezones away from GMT are you? ")
