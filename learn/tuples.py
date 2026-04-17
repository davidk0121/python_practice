# Tuples are like arrays but immutable
tup = (1, 2, 3)
print(tup)
print(tup[0])
print(tup[-1])
#tup[0] = 5 # cannot modify a tuple

# Can be used as key for hash map/set
myMap = {(1,2): 3}
print (myMap[(1,2)])

mySet = set()
mySet.add((1,2))
print((1,2) in mySet)

# Lists can't be keys
# myMap[[3,4]] = 5 # TypeError: unhashable type: 'list'