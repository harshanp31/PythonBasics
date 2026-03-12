#1. Take user input numbers in a loop and stop when the user enters 0

while True:
    num = int(input("Enter a number "))

    if num == 0:
        print("Stopping the loop.")
        break
print("You entered:", num)

#2. Print all characters of a string except vowels

str = input("Enter a string")
len1 = len(str)
i=0
while i < len1:
    if str[i] == "a" or str[i] == "e" or str[i] == "i" or str[i] == "o" or str[i] == "u" or str[i] == "A" or str[i] == "E" or str[i] == "I" or str[i] == "O" or str[i] == "U":
        i += 1
        continue

    print(str[i])
    i += 1


#3. Print numbers from 1 to 50: Skip multiples of 5 Stop if number becomes greater than 40

for i in range(1, 51):

    if i > 40:
        break

    if i % 5 == 0:
        continue

    print(i)