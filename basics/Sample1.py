print("enter 2 nos")
a = int(input())
b = int(input())
print("what would you to perform 1. ADD, 2.SUB 3.MUL,4.DIV")
c=input()
if c=="ADD":
    print(a+b)
elif c=="SUB":
    print(a-b)
elif c=="MUL":
    print(a*b)
elif c=="DIV":
    print(a/b)
else:
    print("Invalid input")
