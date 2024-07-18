#!/usr/bin/python3
(num1, op, num2) = input("Enter a calculation: ").split()
num1 = int(num1)
num2 = int(num2)

if (op == '+'):
    sum = num1 + num2
    print("{} + {} = {}".format(num1, num2, sum))
elif (op == '-'):
    diff = num1 - num2
    print("{} - {} = {}".format(num1, num2, diff))
elif (op == '*'):
    prod = num1 * num2
    print("{} * {} = {}".format(num1, num2, prod))
elif (op == '/'):
    quot = num1 / num2
    print("{} / {} = {}".format(num1, num2, quot))
