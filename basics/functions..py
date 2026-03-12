"""def add(): #defining a function
    a=5
    b=6
    print(a+b)

add()
add() #calling a function

def substractor():
    return a - b

print("enter 2 nos")
a =int(input())
b =int(input())
result = substractor()
print(result)"""

"""print("enter 2 nos")
a =int(input())
b =int(input())
def calculate():
    return a+b,a-b,a*b,a**b,a**b

result = calculate()
print(result)"""
""""
#variable length function
def findmax(*args): #args arguments
    return max(args)
maximum = findmax(55,33,89,9999)
print(maximum)

def findmin(*args): #args arguments
    return min(args)
minimum = findmin(55,33,89,9999)
print(minimum)"""

#anonymus function
add = lambda a,b: a+b
print(add(7,8))











