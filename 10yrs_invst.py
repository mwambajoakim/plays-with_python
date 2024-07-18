#!/usr/bin/python3
(inv, intr, years) = input("Enter your investment, estimated interest and years you plan to invest: ").split()
inv = float(inv)
intr = float(intr)
years = int(years)
inv_yr = (inv + (inv * intr)) * years
print("Your investment, {} will accrue {} after {} years".format(inv, inv_yr, years))
