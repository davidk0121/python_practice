# Binary Search
# Easy
# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.
# Your solution must run in O(logn) time.

# Example 1:
# Input: nums = [-1,0,2,4,6,8], target = 4
# Output: 3

# Example 2:
# Input: nums = [-1,0,2,4,6,8], target = 3
# Output: -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid 
        return -1 
        
#########################################################################################
# Search a 2D Matrix
# Medium
# You are given an m x n 2-D integer array matrix and an integer target.

# Each row in matrix is sorted in non-decreasing order.
# The first integer of every row is greater than the last integer of the previous row.
# Return true if target exists within matrix or false otherwise.

# Can you write a solution that runs in O(log(m * n)) time?

# Example 1:
# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
# Output: true

# Example 2:
# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15
# Output: false

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen, colLen = len(matrix), len(matrix[0])
        top, bot = 0, rowLen - 1
        mid = 0
        while top <= bot:
            mid = (top + bot) // 2
            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                break
        
        l, r = 0, colLen - 1
        m = 0
        while l <= r:
            m = (l + r) // 2
            if matrix[mid][m] < target:
                l = m + 1
            elif matrix[mid][m] > target:
                r = m - 1
            else:
                return True
        return matrix[mid][m] == target

#########################################################################################
# Koko Eating Bananas
# Medium
# You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents 
# the number of hours you have to eat all the bananas.
# You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. 
# If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.
# Return the minimum integer k such that you can eat all the bananas within h hours.

# Example 1:
# Input: piles = [1,4,3,2], h = 9
# Output: 2
# Explanation: With an eating rate of 2, you can eat the bananas in 6 hours. With an eating rate of 1, you would need 10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.

# Example 2:
# Input: piles = [25,10,23,4], h = 4
# Output: 25

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2

            cal = 0
            for p in piles:
                cal += math.ceil(p/k)
            if cal <= h:
                r = k - 1
                res = min(res, k)
            else:
                l = k + 1
        return res
    
#########################################################################################
# Find Minimum in Rotated Sorted Array
# Medium
# You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. 
# For example, the array nums = [1,2,3,4,5,6] might become:
# [3,4,5,6,1,2] if it was rotated 4 times.
# [1,2,3,4,5,6] if it was rotated 6 times.
# Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces 
# the original array.
# Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.
# A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

# Example 1:
# Input: nums = [3,4,5,6,1,2]
# Output: 1

# Example 2:
# Input: nums = [4,5,0,1,2,3]
# Output: 0

# Example 3:
# Input: nums = [4,5,6,7]
# Output: 4

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float("Inf")

        while l <= r:
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[r]:  # is minimum number in the right side
                l = m + 1
            else:                   # is minimum number in the left side
                r = m - 1
        return res

#########################################################################################
# Search in Rotated Sorted Array
# Medium
# You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

# [3,4,5,6,1,2] if it was rotated 4 times.
# [1,2,3,4,5,6] if it was rotated 6 times.
# Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

# You may assume all elements in the sorted rotated array nums are unique,
# A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

# Example 1:
# Input: nums = [3,4,5,6,1,2], target = 1
# Output: 4

# Example 2:
# Input: nums = [3,5,6,0,1,2], target = 4
# Output: -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            #left sorted function
            if nums[m] >= nums[r]:
                if nums[m] > target or nums[r] < target:
                    r = m - 1
                else:
                    l = m + 1
            #right sorted function
            else:
                if nums[m] < target or nums[l] > target:
                    l = m + 1
                else:
                    r = m - 1
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m 
            
            #left sorted function
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else: 
                    r = m - 1
            #right sorted function
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else: 
                    l = m + 1
        return -1

#########################################################################################
# Time Based Key-Value Store
# Medium
# Implement a time-based key-value data structure that supports:

# Storing multiple values for the same key at specified time stamps
# Retrieving the key's value at a specified timestamp
# Implement the TimeMap class:

# TimeMap() Initializes the object.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns the most recent value of key if set was previously called on it and the most recent timestamp for that key prev_timestamp is less than or equal to the given timestamp (prev_timestamp <= timestamp). If there are no values, it returns "".
# Note: For all calls to set, the timestamps are in strictly increasing order.

# Example 1:
# Input:
# ["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]

# Output:
# [null, null, "happy", "happy", null, "sad"]

# Explanation:
# TimeMap timeMap = new TimeMap();
# timeMap.set("alice", "happy", 1);  // store the key "alice" and value "happy" along with timestamp = 1.
# timeMap.get("alice", 1);           // return "happy"
# timeMap.get("alice", 2);           // return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
# timeMap.set("alice", "sad", 3);    // store the key "alice" and value "sad" along with timestamp = 3.
# timeMap.get("alice", 3);           // return "sad"

class TimeMap:

    def __init__(self):
        set = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        

    def get(self, key: str, timestamp: int) -> str:

# Array 
class TimeMap:
    def __init__(self):
        self.keyStore = {}  # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

#########################################################################################

# Median of Two Sorted Arrays
# Hard
# You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. Return the median value among all elements of the two arrays.
# Your solution must run in O(log(m+n)) time.

# Example 1:
# Input: nums1 = [1,2], nums2 = [3]
# Output: 2.0
# Explanation: Among [1, 2, 3] the median is 2.

# Example 2:
# Input: nums1 = [1,3], nums2 = [2,4]
# Output: 2.5

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:


class Solution:
    def get_kth(self, a: List[int], m: int, b: List[int], n: int, k: int, a_start: int = 0, b_start: int = 0) -> int:
        if m > n:
            return self.get_kth(b, n, a, m, k, b_start, a_start)
        if m == 0:
            return b[b_start + k - 1]
        if k == 1:
            return min(a[a_start], b[b_start])

        i = min(m, k // 2)
        j = min(n, k // 2)

        if a[a_start + i - 1] > b[b_start + j - 1]:
            return self.get_kth(a, m, b, n - j, k - j, a_start, b_start + j)
        else:
            return self.get_kth(a, m - i, b, n, k - i, a_start + i, b_start)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left = (len(nums1) + len(nums2) + 1) // 2
        right = (len(nums1) + len(nums2) + 2) // 2
        return (self.get_kth(nums1, len(nums1), nums2, len(nums2), left) +
                self.get_kth(nums1, len(nums1), nums2, len(nums2), right)) / 2.0