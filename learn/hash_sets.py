# Hash Set
mySet = set()
mySet.add(1)
mySet.add(2)
print(mySet) # output: {1, 2}
print(len(mySet)) # output: 2

print(1 in mySet) # output: True
print(2 in mySet) # output: True
print(3 in mySet) # output: False

mySet.remove(2)
print(2 in mySet) # output: False
#--------------------
# list to set
print(set([1, 2, 3]))
# Set comprehension
mySet = {i for i in range(5)}
print(mySet) # output: {0, 1, 2, 3, 4}