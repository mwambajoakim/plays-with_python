#!/usr/bin/python3

# main - program to convert temperature to farenheit
# Author: Joakim Mwamba
# Date: 22/07/2024

def main():
    print("""This program will convert temperature to farenheit.
    It will ask you for input as celsius.""")
    celsius = input("What is the temperature in Celsius? ")
    celsius = float(celsius)
    farenheit = 9/5 * celsius + 32
    print(f"The temperature in farenheit is {farenheit}")
    input("Press the <Enter> key to quit")


main()
