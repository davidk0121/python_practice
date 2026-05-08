
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
        l, r = 0, 1
        maxRes = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                sum = prices[r] - prices[l]
                maxRes = max(sum, maxRes)
                r += 1
            else:
                l = r 
                r += 1
        return maxRes

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
        l = 0 
        res = 0 
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, len(charSet))
        return res
    
#########################################################################################
# Longest Repeating Character Replacement
# Medium

# Hints
# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string 
# and replace them with any other uppercase English character.
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
        count = {}
        res = 0 
        l, r = 0, 0 

        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)
            while ((r - l + 1) - max(count.values())) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res 
        
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
        if len(s1) > len(s2): return False

        s1Count, s2Count = [0] * 26, [0] * 26

        # count initials
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # match count initials
        matches = 0 
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        # sliding window
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            rIndex = ord(s2[r]) - ord('a')
            s2Count[rIndex] += 1 # moving one to the right so take one in to the window
            if s1Count[rIndex] == s2Count[rIndex]:
                matches += 1 # plus 1 when the match was added
            elif s1Count[rIndex] + 1 == s2Count[rIndex]:
                matches -= 1 # minus 1 when the duplicate was added

            lIndex = ord(s2[l]) - ord('a')
            s2Count[lIndex] -= 1 # moving one to the right so take one out from window
            if s1Count[lIndex] == s2Count[lIndex]:
                matches += 1 # plus 1 when the duplicate is removed
            elif s1Count[lIndex] - 1 == s2Count[lIndex]:
                matches -= 1 # minus 1 when the match was removed
            l += 1
        return matches == 26
# Time: O(n)
# Space: O(1)
        
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
        if t == "": return ""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
# Time: O(n+m)
# Space: O(m)


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
        

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # index
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output
# Time: O(n)
# Space: O(n)