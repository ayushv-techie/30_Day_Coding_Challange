# Day 2: Write a program to find the largest of three numbers.

num1 = int(input("Enter the first no."))
num2 = int(input("Enter the second no."))
num3 = int(input("Enter the third no."))

if num1>= num2 and num1>=num3:
    print(f"Largest no. is {num1}")
elif num2>= num1 and num2>=num3:
    print(f"Largest no. is {num2}")
else:
    print(f"Largest no. is {num3}")