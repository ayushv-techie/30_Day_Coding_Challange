# Day 4: Write a program to swap two numbers using only two variables and without using any arithmetic operators.

def swap_numbers(a, b):
    print(f"Before swapping: a = {a}, b = {b}")
    a = a ^ b  
    b = a ^ b  
    a = a ^ b  
    print(f"After swapping: a = {a}, b = {b}")

a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))
swap_numbers(a, b)
