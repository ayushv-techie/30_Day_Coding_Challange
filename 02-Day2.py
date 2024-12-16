# Day 10: Wap to get a number from user and check whether it is Palindrome.

def is_palindrome(s):
 return s == s[::-1]
string = input("Enter a string: ")
if is_palindrome(string):
 print("Palindrome")
else:
 print("Not a palindrome")
