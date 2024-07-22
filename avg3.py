#!/usr/bin/python3

# main - program to calculate average
# Author: Joakim Mwamba

def main():
    print("""This program wwill calculate the average
    of three numbers.

    Please enter some input""")

    (score1, score2, score3) = input("What are the scores? ").split()
    score1 = int(score1)
    score2 = int(score2)
    score3 = int(score3)

    avg = (score1 + score2 + score3) / 3

    print(f"The average is {avg}")
    input("Press <Enter> to exit")


main()
