# Day 6: Wap to get a number from user and calculate its factorial and keep the case of factorial of "0" as well.

def factorial(n):
 if n == 0:
  return 1
 else:
  return n * factorial(n - 1)
num = int(input("Enter a number: "))
print("Factorial:", factorial(num))