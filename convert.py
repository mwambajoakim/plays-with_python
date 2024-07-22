#!/usr/bin/python3

# main - program to convert temperature to farenheit
# Author: Joakim Mwamba
# Date: 22/07/2024

def main():
    print("This program will convert temperature to farenheit.")
    celsius = 0
    for i in range(10):
        celsius += 10
        farenheit = 9/5 * celsius + 32
        print(f"{celsius}                         {farenheit}")


main()
