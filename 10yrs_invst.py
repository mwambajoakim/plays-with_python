#!/usr/bin/python3
(inv, intr, years) = input("Enter your investment,"
                           "interest and years to invest: ").split()
inv = float(inv)
intr = float(intr) * .01
years = int(years)
for i in range(years):
    inv = inv + (inv * intr)
print("Your investment will accrue {:.2f} after {} years.".format(inv, years))
