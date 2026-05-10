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

#########################################################################################

#########################################################################################

#########################################################################################

#########################################################################################
