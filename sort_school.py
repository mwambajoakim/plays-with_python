#!/usr/bin/python3
age = eval(input("Enter your age: "))
if (age == 5):
    print("Go to Kindergarten!")
elif (age >= 6 and age <= 17):
    print("Go to Grades 1 through to 12!")
elif (age >= 17 and age <= 25):
    print("Go to College!")
else:
    print("You are done with school!")
