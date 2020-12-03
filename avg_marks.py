"""
Name: avg_marks.py
Purpose: To calculate the total average between 4 course averages

Athor: Stefan Tuczynski

Date: 02/12/2020
"""

#These lines takes the users four course's average
Course_One = int(input("Course One Average: "))
Course_Two = int(input("Course Two Average: "))
Course_Three = int(input("Course Three Average: "))
Course_Four = int(input("Course Four Average: "))

#This line calculates the total average between the 4 courses
print("Your total average is: " + str((Course_One + Course_Two + Course_Three + Course_Four) / 4) + "%")
