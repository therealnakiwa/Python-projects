# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:10:25 2026

@author: julia
"""

def main():
    # Header decoration
    print("***********************************")
    print("*      TEST SCORE CALCULATOR      *")
    print("***********************************")

    # Input - Getting 8 scores
    s1 = float(input("Enter score 1: "))
    s2 = float(input("Enter score 2: "))
    s3 = float(input("Enter score 3: "))
    s4 = float(input("Enter score 4: "))
    s5 = float(input("Enter score 5: "))
    s6 = float(input("Enter score 6: "))
    s7 = float(input("Enter score 7: "))
    s8 = float(input("Enter score 8: "))

    # Table Header
    print("\nScore\t\tNumeric Grade\tLetter Grade")
    print("----------------------------------------------------")

    # Display individual scores and grades
    # Using a list or separate calls is fine; here we call determine_grade for each
    print(f"score 1:\t\t{s1:.1f}\t\t\t{determine_grade(s1)}")
    print(f"score 2:\t\t{s2:.1f}\t\t\t{determine_grade(s2)}")
    print(f"score 3:\t\t{s3:.1f}\t\t\t{determine_grade(s3)}")
    print(f"score 4:\t\t{s4:.1f}\t\t\t{determine_grade(s4)}")
    print(f"score 5:\t\t{s5:.1f}\t\t\t{determine_grade(s5)}")
    print(f"score 6:\t\t{s6:.1f}\t\t\t{determine_grade(s6)}")
    print(f"score 7:\t\t{s7:.1f}\t\t\t{determine_grade(s7)}")
    print(f"score 8:\t\t{s8:.1f}\t\t\t{determine_grade(s8)}")

    # Calculate and display average
    avg = calc_average(s1, s2, s3, s4, s5, s6, s7, s8)
    final_letter = determine_grade(avg)

    print("----------------------------------------------------")
    print(f"Average of all the scores for the course is a {avg:.1f} %.")
    print(f"The letter grade for the course is a '{final_letter}'.")

# Function (return): Accepts 8 scores and returns the average
def calc_average(n1, n2, n3, n4, n5, n6, n7, n8):
    return (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8) / 8

# Function (return): Accepts a score and returns a letter grade based on the table
def determine_grade(score):
    if score >= 99:
        return "A+"
    elif score >= 92:
        return "A"
    elif score >= 90:
        return "A-"
    elif score >= 88:
        return "B+"
    elif score >= 82:
        return "B"
    elif score >= 80:
        return "B-"
    elif score >= 78:
        return "C+"
    elif score >= 72:
        return "C"
    elif score >= 70:
        return "C-"
    elif score >= 68:
        return "D+"
    elif score >= 62:
        return "D"
    elif score >= 60:
        return "D-"
    else:
        return "F"

if __name__ == "__main__":
    main()

