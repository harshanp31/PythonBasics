grade = int(input("Enter the score: "))
""""
if grade >= 90:
    print("You scored Grade A")
elif 75 <= grade <= 89:
    print("You scored Grade B")
elif 50 <= grade <= 74:
    print("You scored Grade C")
elif grade <= 49:
    print("You scored Grade D")
else:
    print("Failed")"""

if grade >= 90:
    print("You scored Grade A")
elif (grade >=75) and (grade <= 89):
    print("You scored Grade B")
elif (grade >=50) and (grade <= 74):
    print("You scored Grade C")
elif (grade >= 49) and (grade <= 35):
    print("You scored Grade D")
else:
    print("Failed")



