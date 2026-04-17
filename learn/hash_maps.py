# Hash Maps (Dictionaries)
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77
print(myMap) # output: {'alice': 88, 'bob': 77}
print(len(myMap)) # output: 2

myMap["alice"] = 80
print(myMap["alice"]) # output: 80

print ("alice" in myMap) # output: True
myMap.pop("alice")
print ("alice" in myMap) # output: False

myMap = { "alice":90, "bob":70}
print(myMap)
#--------------------
# Dict comprehension
myMap = {i: 2*i for i in range(3)}
print(myMap) # output: {0: 0, 1: 2, 2: 4}
#--------------------
# Looping through maps
myMap = { "alice":90, "bob":70}

for key in myMap:
    print(key, myMap[key])

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key, val)