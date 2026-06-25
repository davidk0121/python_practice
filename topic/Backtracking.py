
# Subsets
# Medium
# Given an array nums of unique integers, return all possible subsets of nums.
# The solution set must not contain duplicate subsets. You may return the solution in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [7]
# Output: [[],[7]]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            


        dfs(0)
        return res

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

#########################################################################################
# Combination Sum
# Medium
# You are given an array of distinct integers nums and a target integer target. Your task is to return a list of all unique combinations of nums where the 
# chosen numbers sum to target.
# The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the 
# same, otherwise they are different.
# You may return the combinations in any order and the order of the numbers in each combination can be in any order.

# Example 1:
# Input:
# nums = [2,5,6,9]
# target = 9
# Output: [[2,2,5],[9]]
# Explanation:
# 2 + 2 + 5 = 9. We use 2 twice, and 5 once.
# 9 = 9. We use 9 once.

# Example 2:
# Input:
# nums = [3,4,5]
# target = 16
# Output: [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]

# Example 3:
# Input:
# nums = [3]
# target = 5
# Output: []

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return 
            if i >= len(nums) or total > target:
                return 
            
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
#########################################################################################
# Combination Sum II
# Medium
# You are given an array of integers candidates, which may contain duplicates, and a target integer target. Your task is to return a list of all unique combinations 
# of candidates where the chosen numbers sum to target.
# Each element from candidates may be chosen at most once within a combination. The solution set must not contain duplicate combinations.
# You may return the combinations in any order and the order of the numbers in each combination can be in any order.

# Example 1:
# Input: candidates = [9,2,2,4,6,1,5], target = 8
# Output: [
#   [1,2,5],
#   [2,2,4],
#   [2,6]
# ]

# Example 2:
# Input: candidates = [1,2,3,4,5], target = 7
# Output: [
#   [1,2,4],
#   [2,5],
#   [3,4]
# ]

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
#########################################################################################
# Permutations
# Medium
# Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
# Input: nums = [7]
# Output: [[7]]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
#########################################################################################
# Subsets II
# Medium
# You are given an array nums of integers, which may contain duplicates. Return all possible subsets.
# The solution must not contain duplicate subsets. You may return the solution in any order.

# Example 1:
# Input: nums = [1,2,1]
# Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]

# Example 2:
# Input: nums = [7,7]
# Output: [[],[7], [7,7]]

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
#########################################################################################
# Generate Parentheses
# Medium
# You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

# Example 1:
# Input: n = 1
# Output: ["()"]

# Example 2:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# You may return the answer in any order.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
#########################################################################################
# Word Search
# Medium
# Given a 2-D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false.
# For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. 
# The same cell may not be used more than once in a word.

# Example 1:
# Input: 
# board = [
#   ["A","B","C","D"],
#   ["S","A","A","T"],
#   ["A","C","A","E"]
# ],
# word = "CAT"
# Output: true

# Example 2:
# Input: 
# board = [
#   ["A","B","C","D"],
#   ["S","A","A","T"],
#   ["A","C","A","E"]
# ],
# word = "BAT"
# Output: false

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
#########################################################################################
# Palindrome Partitioning
# Medium
# Given a string s, split s into substrings where every substring is a palindrome. Return all possible lists of palindromic substrings.
# You may return the solution in any order.

# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:
# Input: s = "a"
# Output: [["a"]]

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
#########################################################################################
# Letter Combinations of a Phone Number
# Medium
# You are given a string digits made up of digits from 2 through 9 inclusive.
# Each digit (not including 1) is mapped to a set of characters as shown below:
# A digit could represent any one of the characters it maps to.
# Return all possible letter combinations that digits could represent. You may return the answer in any order.
# Phone keypad letter mapping

# Example 1:
# Input: digits = "34"
# Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]

# Example 2:
# Input: digits = ""
# Output: []

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
#########################################################################################