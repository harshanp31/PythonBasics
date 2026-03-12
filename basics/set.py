#set -->A set in python is used to store a collection of items or elemenst that is unordered , mutable & ,that donot allow duplicates elements
#heterogenous unique elements are permitted
#empty set
set1 = {}
print(set1)

set2 = {1,2,3}
print(set2)

list1 = [1,2,3,'h',5,6,7,8,"hello"]
set2.update(list1)
print(set2)

tuple1 = ("python","java",4,7,"javascript")
set2.add(tuple1)
print(set2)

#sorted
set3 = {5,22,7,1,34,0,6.7,-2}
print(sorted(set3)) #sorting


#frozen set
x = frozenset(set3)
#x.add(25) we can't add elements to frozen set can perform update , new operations


print(x)
print(sorted(x))

#clear
set2.clear()
print(set2)


