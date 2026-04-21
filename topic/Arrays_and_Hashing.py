class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            count = 0 
            if (num - 1) not in numSet:
                while (num + count) in numSet:
                    count += 1
            longest = max(longest, count)

        return longest