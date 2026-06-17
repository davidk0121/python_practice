

#########################################################################################
# Kth Largest Element in a Stream
# Easy
# Design a class to find the kth largest integer in a stream of values, including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.

# Implement the following methods:
# constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
# int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.
# Example 1:
# Input:
# ["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]
# Output:
# [null, 3, 3, 3, 5, 6]

# Explanation:
# KthLargest kthLargest = new KthLargest(3, [1, 2, 3, 3]);
# kthLargest.add(3);   // return 3
# kthLargest.add(5);   // return 3
# kthLargest.add(6);   // return 3
# kthLargest.add(7);   // return 5
# kthLargest.add(8);   // return 6

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        

    def add(self, val: int) -> int:

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # minHeap with K largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

#########################################################################################
# Last Stone Weight
# Easy
# You are given an array of integers stones where stones[i] represents the weight of the ith stone.
# We want to run a simulation on the stones as follows:

# At each step we choose the two heaviest stones, with weight x and y and smash them togethers
# If x == y, both stones are destroyed
# If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# Continue the simulation until there is no more than one stone remaining.

# Return the weight of the last remaining stone or return 0 if none remain.

# Example 1:
# Input: stones = [2,3,6,2,4]
# Output: 1

# Explanation:
# We smash 6 and 4 and are left with a 2, so the array becomes [2,3,2,2].
# We smash 3 and 2 and are left with a 1, so the array becomes [1,2,2].
# We smash 2 and 2, so the array becomes [1].

# Example 2:
# Input: stones = [1,2]
# Output: 1

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
            
        stones.append(0)
        return abs(stones[0])

#########################################################################################
# K Closest Points to Origin
# Medium
# Topics
# Company Tags
# Hints
# You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are also given an integer k.
# Return the k closest points to the origin (0, 0).
# The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).
# You may return the answer in any order.

# Example 1:
# Input: points = [[0,2],[2,2]], k = 1
# Output: [[0,2]]
# Explanation : The distance between (0, 2) and the origin (0, 0) is 2. The distance between (2, 2) and the origin is sqrt(2^2 + 2^2) = 2.82842. So the closest point to the origin is (0, 2).

# Example 2:
# Input: points = [[0,2],[2,0],[2,2]], k = 2
# Output: [[0,2],[2,0]]
# Explanation: The output [2,0],[0,2] would also be accepted.

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res


#########################################################################################
# Kth Largest Element in an Array
# Medium
# Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.
# By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.
# Follow-up: Can you solve it without sorting?

# Example 1:
# Input: nums = [2,3,1,5,4], k = 2
# Output: 4

# Example 2:
# Input: nums = [2,3,1,1,5,5,4], k = 3
# Output: 4

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:


#########################################################################################
# Task Scheduler
# Medium
# You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.
# Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.
# The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.
# Return the minimum number of CPU cycles required to complete all tasks.

# Example 1:
# Input: tasks = ["X","X","Y","Y"], n = 2
# Output: 5
# Explanation: A possible sequence is: X -> Y -> idle -> X -> Y.

# Example 2:
# Input: tasks = ["A","A","A","B","C"], n = 3
# Output: 9
# Explanation: A possible sequence is: A -> B -> C -> Idle -> A -> Idle -> Idle -> Idle -> A.

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:


#########################################################################################
# Design Twitter
# Medium
# Implement a simplified version of Twitter which allows users to post tweets, follow/unfollow each other, and view the 10 most recent tweets within their own news feed.
# Users and tweets are uniquely identified by their IDs (integers).

# Implement the following methods:
# Twitter() Initializes the twitter object.
# void postTweet(int userId, int tweetId) Publish a new tweet with ID tweetId by the user userId. You may assume that each tweetId is unique.
# List<Integer> getNewsFeed(int userId) Fetches at most the 10 most recent tweet IDs in the user's news feed. Each item must be posted by users who the user is following or by the user themself. Tweets IDs should be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId follows the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId unfollows the user with ID followeeId.

# Example 1:
# Input:
# ["Twitter", "postTweet", [1, 10], "postTweet", [2, 20], "getNewsFeed", [1], "getNewsFeed", [2], "follow", [1, 2], "getNewsFeed", [1], "getNewsFeed", [2], "unfollow", [1, 2], "getNewsFeed", [1]]
# Output:
# [null, null, null, [10], [20], null, [20, 10], [20], null, [10]]

# Explanation:
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 10); // User 1 posts a new tweet with id = 10.
# twitter.postTweet(2, 20); // User 2 posts a new tweet with id = 20.
# twitter.getNewsFeed(1);   // User 1's news feed should only contain their own tweets -> [10].
# twitter.getNewsFeed(2);   // User 2's news feed should only contain their own tweets -> [20].
# twitter.follow(1, 2);     // User 1 follows user 2.
# twitter.getNewsFeed(1);   // User 1's news feed should contain both tweets from user 1 and user 2 -> [20, 10].
# twitter.getNewsFeed(2);   // User 2's news feed should still only contain their own tweets -> [20].
# twitter.unfollow(1, 2);   // User 1 unfollows user 2.
# twitter.getNewsFeed(1);   // User 1's news feed should only contain their own tweets -> [10].

class Twitter:

    def __init__(self):
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        

    def getNewsFeed(self, userId: int) -> List[int]:
        

    def follow(self, followerId: int, followeeId: int) -> None:
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        

class Twitter:

    def __init__(self):
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        

    def getNewsFeed(self, userId: int) -> List[int]:
        

    def follow(self, followerId: int, followeeId: int) -> None:
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        

#########################################################################################
# Find Median From Data Stream
# Hard