
# Best Time to Buy and Sell Stock

# Hints
# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

# Example 1:
# Input: prices = [10,1,5,6,7,1]
# Output: 6
# Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

# Example 2:
# Input: prices = [10,8,7,5,2]
# Output: 0
# Explanation: No profitable transactions can be made, thus the max profit is 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:


#########################################################################################
# Longest Substring Without Repeating Characters
# Medium

# Hints
# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.

# Example 1:
# Input: s = "zxyzxyz"
# Output: 3
# Explanation: The string "xyz" is the longest without duplicate characters.

# Example 2:
# Input: s = "xxxx"
# Output: 1

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

#########################################################################################
# Longest Repeating Character Replacement
# Medium

# Hints
# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

# Example 1:
# Input: s = "XYYX", k = 2
# Output: 4
# Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

# Example 2:
# Input: s = "AAABABB", k = 1
# Output: 5

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
#########################################################################################
# Permutation in String
# Medium

# Hints
# You are given two strings s1 and s2.

# Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

# Both strings only contain lowercase letters.

# Example 1:
# Input: s1 = "abc", s2 = "lecabee"
# Output: true
# Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

# Example 2:
# Input: s1 = "abc", s2 = "lecaabee"
# Output: false

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
#########################################################################################
# Minimum Window Substring
# Hard

# Hints
# Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

# You may assume that the correct output is always unique.

# Example 1:
# Input: s = "OUZODYXAZV", t = "XYZ"
# Output: "YXAZ"
# Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

# Example 2:
# Input: s = "xyz", t = "xyz"
# Output: "xyz"

# Example 3:
# Input: s = "x", t = "xy"
# Output: ""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
#########################################################################################

# Sliding Window Maximum
# Hard

# Hints
# You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

# Return a list that contains the maximum element in the window at each step.

# Example 1:
# Input: nums = [1,2,1,0,4,2,6], k = 3
# Output: [2,2,4,4,6]

# Explanation:
# Window position            Max
# ---------------           -----
# [1  2  1] 0  4  2  6        2
#  1 [2  1  0] 4  2  6        2
#  1  2 [1  0  4] 2  6        4
#  1  2  1 [0  4  2] 6        4
#  1  2  1  0 [4  2  6]       6

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        


