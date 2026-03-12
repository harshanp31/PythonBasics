#while loop
#Based on condition it works
#Entry controlled loop
"""str = "hi this is harsha how are you"
i = 0
counter = 0
#len() -->function find the length of the string
length = len(str)
print(length)
while i < length:
    if str[i] == "a" or str[i] == "e" or str[i] == "i" or str[i] == "o" or str[i] == "u":
        counter += 1
    i+=1
print("no of vowels in the strings is ",counter)"""

#while else

str = "hi this is harsha how are you"
i = 0
counter = 0
#len() -->function find the length of the string
length = len(str)
print(length)
while i > length:
    if str[i] == "a" or str[i] == "e" or str[i] == "i" or str[i] == "o" or str[i] == "u":
        counter += 1
    i+=1

else:
    print("no vowels found in string")

print("no of vowels in the strings is ",counter)





