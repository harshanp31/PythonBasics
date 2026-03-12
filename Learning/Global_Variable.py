#To create a global variable inside a function, you can use the global keyword.
def view():
    global a # x is a global variable
    a="welcome to the world"
    return a

y=view()
print(y)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)



