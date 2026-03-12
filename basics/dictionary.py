#python dictionary is a data structure that stores the value in key values
#n dictionary can be of any data type and can be duplicated , whereas key can't be repeated and must be immutable
#how to create a dictionary
d1 = {1:"apple",2:"organge",3:"banana"}
print(d1)
print(d1.get(1)) #inbuilt method used to get a value from a dicitionary associatd with the key
print(d1[3])
#creation of dict
d2 = dict(a="parrot",b="pigeon",c="crow")
print(d2)

#updation
d2['a'] = "eagle"
print(d2)

#Remove
del d2['a']
print(d2)

