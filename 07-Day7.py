# Day 5: Write a program to get a year as input from user and check whether it is a leap year.

def is_leap_year(year):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    return True
  else:
    return False
year = int(input("Enter a year: "))
if is_leap_year(year):
 print("Leap year")
else:
 print("Not a leap year")