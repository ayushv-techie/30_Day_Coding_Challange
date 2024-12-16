# Day 9: Write a program to print the triangle of stars using loops .

n=10
for i in range(1, n + 1):
 print("*" * i)

        #   For Pyramid pattern

for i in range(n):
 print(" " * (n - i - 1) + "*" * (2 * i + 1))