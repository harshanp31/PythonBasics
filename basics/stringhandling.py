#String Handling
#String-->It is collection / sequence of characters
#+ve indexing -->its starts from zero
#-ve indexing -->its starts from -1 [right to left travers]
message =   "this is a sample is message"
"""print(message[0])
print(message[4])
print(message[5])
print(message[-1])"""
length = len(message)
for i in range(length):
    print(message[i])

#Slicing -->to extract
print(message[1:5])
print(message[:5])

#Concatenation -->to combine mutltiple string (+)
print("hello " + message)

#Case changing -->case conversion
print(message.upper())
print(message.lower())
print(message.capitalize())
print(message.title()) #each word in the sentence is changes to upper case

#searching
print("harsha" in message)
print("harsha" not in message)

#Replacing
msg = message.replace("is","that")
print(msg)




