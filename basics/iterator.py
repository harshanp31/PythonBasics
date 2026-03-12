list1 =[1,2,6,4,99,44,56]
iterator = iter(list1) #iter is a keyword that is used to initialise iterator
"""print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))"""
length = len(list1)
item = 1
for item in range(length):
    print(next(iterator))
    item += 1


