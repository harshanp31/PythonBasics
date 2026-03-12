#1. Write a program to input a string and print its length

"""str1 = input("Enter a string")
length = len(str1)
print("The length of the string is", length)"""


# 2. Read a message from user and Convert a string to: (a)Uppercase (b)Lowercase (c) Replace all spaces with underscores (_). (d) Find the first and last character of a string
str2 = input("Enter a string")
print("Uppercase :", str2.upper())
print("Lowercase :", str2.lower())

msg = str2.replace(" ","_")
print(msg)
print("First character of the string is", str2[0])
print("Last character of the string is ",str2[-1])
