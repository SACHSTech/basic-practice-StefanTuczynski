"""
Name: oz_to_ml.pz
Purpose: To calculate the amount of ml required to feed people being given ounces
Creator: Stefan Tuczynski
Date: 02/12/2020
"""

#User input lines
print("--- Welcome to the Onces to Millileter converter ---")
oz = float(input("Amount of onces: "))
people = int(input("Amount of people needed to be served: "))

#Conversion line#
ml = (oz * 29.5735)

#Final calculations for milliters required
ml_required = (ml * people)
print ("You will need " + str(ml_required) + "ml to feed " + str(people))
print("--- Thank you for using our converter! ---")
