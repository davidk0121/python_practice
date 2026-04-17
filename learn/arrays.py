# Arrys (called lists in python)
arr = [1, 2, 3]
print(arr) # output: [1, 2, 3]

# Can be used as a stack 
arr.append(4)
arr.append(5)
print(arr) # output: [1, 2, 3, 4]

arr.pop()
print(arr) # output: [1, 2, 3, 4]

arr.insert(1, 7)
print(arr) # output: [1, 7, 2, 3, 4]  #O(n) time

arr[0] = 0
arr[3] = 0
print(arr) # output: [0, 7, 2, 0, 4]

# -------------------

# initialize arr of size n with default value of 1
n = 5
arr = [1] * n
print(arr) # output: [1, 1, 1, 1, 1]
print(len(arr)) # output: 5

arr = [1, 2, 3]
print(arr[-1]) # output: 3 # last element
print(arr[-2]) # output: 2 # second to last element

# -------------------
# Sublists (slicing)
arr = [1, 2, 3, 4]
print(arr[1:3]) # output: [2, 3]

# -------------------
# Unpacking
a, b, c = [1, 2, 3]
print(a, b, c) # output: 1 2 3
# -------------------
# Loop through arrays
nums = [1, 2, 3]

#Using index
for i in range(len(nums)):
    print(nums[i])

#Without index
for num in nums:
    print(num)

#with index and value
for i, num in enumerate(nums):
    print(i, num)
# -------------------
# Loop through multiple arrays simultaneously with unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)
# -------------------
# Reverse an array
arr = [1, 2, 3, 4]
print(arr[::-1]) # output: [4, 3, 2, 1]
arr.reverse()
print(arr) # output: [4, 3, 2, 1]