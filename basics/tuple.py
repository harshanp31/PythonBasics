#tuple --> is a ordered,immutable cllection of elements.tubple are similar to list in that they can store multiple itmes in a single variable and items are access from interger starting from zero. once a tuple is created its elements cann't be changed ,added
empty_tuble = () #-->Tuple creation
print(empty_tuble)
tuple1 = (1,2.32,'h',"Hello")
print(tuple1)

#tuple() -->creating a tuple from list

list1 = [1,2,'f','g',"Hello"]
new_tuple = tuple(list1)
print(list1)
print(new_tuple)

#repatative tuple
rep_tuple = (10,)*3
rep_tuple1 = ("python ")*4
print(rep_tuple1)
print(rep_tuple)
