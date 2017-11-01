# Author: Patrick Canny
# Hackerrank Algorithms Problem
# HackerLand University has the following grading policy:
#
# Every student receives a grade in the inclusive range from 0 to 100.
# Any grade less than 40  is a failing grade.
# Sam is a professor at the university and likes to round each student's grade according to these rules:
#
# 1. If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of .
# 2. If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
#
# For example, grade 84 will be rounded to 85 but grade 29 will not be rounded because the rounding would result in a number that is less than 40.
#
# Given the initial value of grade for each of Sam's students, write code to automate the rounding process.
# For each grade, round it according to the rules above and print the result on a new line.
#
# Input Format
#
# The first line contains a single integer denoting  n (the number of students).
# Each line i of the n subsequent lines contains a single integer, grade, denoting student i's grade.

import sys

def solve(grades):
    newgrades = []
    if len(grades) == 0:
        return
    for grade in grades:
        if grade % 5 != 0 and grade > 37:
            newgrade = (5 - grade%5) + grade
            if grade%5 < 3:
                newgrades.append(grade)
            else:
                newgrades.append(newgrade)
        else:
            newgrades.append(grade)

    return newgrades


n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))
