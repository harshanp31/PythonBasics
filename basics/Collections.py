#Colloections
#List -->unordered collection of elements and we can access the elements using index, index starts from 0
list1 = [1,2,4,'f',"hi"]
print(list1)
#repetitive list
replist = [5]*10
print(replist)

#fetching elements from the a list
print(list1[0])
print(list1[-1])
#insert()
list1.insert(1,"xx")
print(list1)

#append()
list1.append("end")
print(list1)

#index()
print(list1.index("end"))

#sort
list2 = [5,2,99,323,66,32,2,5]
list2.sort()
print(list2)
list2.reverse()
print(list2)

#count -->To find the occurance of particular elements

print(list2.count(5))


