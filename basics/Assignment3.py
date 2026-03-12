#Print even numbers from 1 to 30 using for loop
for i in range(1,31):
    if i%2 == 0:
        print(i)

#2. Read a number from user until user enters N for the prompt "Do you want to continue? Y/N"
while True:
    num = int(input("Enter a number: "))
    print("You entered:", num)
    choice = input("Do you want to continue? Y/N: ")
    if choice == 'n' or choice == 'N':
        break




