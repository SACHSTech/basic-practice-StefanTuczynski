"""
Name: cake_jog.py
Purpose: To calculate how many km you have to jog to burn off a specified amount of cake

Author: Stefan Tuczynski

Date: 03/12/2020
"""

#Asks user how many pieces of cake did he/she eat
print("--- Welcome to the online cake to exercise converter! ---")
cake_pieces = float(input("How many pieces of cake did you eat: "))

#Input
cake_cal = float(225)
cal_eaten = (cake_pieces * cake_cal)
jogging = int(100)

#Tells user how many km he/she needs to jog
print ("You need to jog ", cal_eaten / jogging , "km to burn off all of the cake!")
print ("--- Thank you for using the online cake to exercise converter! ---")

