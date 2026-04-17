# Sorting
arr = [5, 4, 7, 3, 8]
arr.sort()
print(arr) # output: [3, 4, 5, 7, 8]

# Sort in descending order
arr.sort(reverse=True)
print(arr) # output: [8, 7, 5, 4, 3]


arr = ["bob", "alice", "charlie"]
arr.sort()
print(arr) # output: ['alice', 'bob', 'charlie'] 

# Custom sorting (by length of string)
arr.sort(key=lambda x : len(x))   
print(arr) # output: ['bob', 'alice', 'charlie']  # sorted by length of string 