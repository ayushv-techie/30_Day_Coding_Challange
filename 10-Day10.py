# Day 8: Write a program to check if the given number is Armstrong or not

def is_armstrong(num):
    digits = str(num)
    order = len(digits) 
    armstrong_sum = sum(int(digit) ** order for digit in digits)
    return armstrong_sum == num

number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
