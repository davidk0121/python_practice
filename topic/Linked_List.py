# Reverse Linked List
# Easy
# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

# Example 1:
# Input: head = [0,1,2,3]
# Output: [3,2,1,0]

# Example 2:
# Input: head = []
# Output: []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

#########################################################################################
# Merge Two Sorted Linked Lists
# Easy
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

# The new list should be made up of nodes from list1 and list2.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,5]
# Output: [1,1,2,3,4,5]

# Example 2:
# Input: list1 = [], list2 = [1,2]
# Output: [1,2]

# Example 3:
# Input: list1 = [], list2 = []
# Output: []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        
        if list1:
            node.next = list1
        elif list2:
            node.next = list2
        
        return dummy.next
        
#########################################################################################
# Linked List Cycle Detection
# Easy
# Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.
# There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.
# Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.
# Note: index is not given to you as a parameter.

# Example 1:
# Input: head = [1,2,3,4], index = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:
# Input: head = [1,2], index = -1
# Output: false

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

#########################################################################################
# Reorder Linked List
# Medium
# You are given the head of a singly linked-list.
# The positions of a linked list of length = 7 for example, can intially be represented as:
# [0, 1, 2, 3, 4, 5, 6]
# Reorder the nodes of the linked list to be in the following order:
# [0, 6, 1, 5, 2, 4, 3]
# Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:
# [0, n-1, 1, n-2, 2, n-3, ...]
# You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

# Example 1:
# Input: head = [2,4,6,8]
# Output: [2,8,4,6]

# Example 2:
# Input: head = [2,4,6,8,10]
# Output: [2,10,4,8,6]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1) find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2) reverse second half
        second = slow.next      # store second half
        prev = None
        slow.next = None        # make first half end point None
        while second:
            temp = second.next  # next to temp
            second.next = prev  # make next value eqaul to previous value (put behind prev)
            prev = second       # assign - 
            second = temp       # assign - 

        # 3) merge two halves
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        
        
#########################################################################################
# Remove Node From End of Linked List
# Medium
# You are given the beginning of a linked list head, and an integer n.
# Remove the nth node from the end of the list and return the beginning of the list.

# Example 1:
# Input: head = [1,2,3,4], n = 2
# Output: [1,2,4]

# Example 2:
# Input: head = [5], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 2
# Output: [2]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        i = 1
        while i <= n and right:
            right = right.next
            i += 1

        while right:
            left = left.next
            right = right.next
        
        #delete
        left.next = left.next.next
        return dummy.next

#########################################################################################

# Copy Linked List with Random Pointer
# Medium
# You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which 
# may point to any node in the list, or null.
# Create a deep copy of the list.
# The deep copy should consist of exactly n new nodes, each including:
# - The original value val of the copied node
# - A next pointer to the new node corresponding to the next pointer of the original node
# - A random pointer to the new node corresponding to the random pointer of the original node
# Note: None of the pointers in the new list should point to nodes in the original list.
# Return the head of the copied linked list.

# In the examples, the linked list is represented as a list of n nodes. Each node is represented as a pair of [val, random_index] where 
# random_index is the index of the node (0-indexed) that the random pointer points to, or null if it does not point to any node.

# Example 1:
# Input: head = [[3,null],[7,3],[4,0],[5,1]]
# Output: [[3,null],[7,3],[4,0],[5,1]]

# Example 2:
# Input: head = [[1,null],[2,2],[3,2]]
# Output: [[1,null],[2,2],[3,2]]

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

cclass Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None : None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]

#########################################################################################

# Add Two Numbers
# Medium
# You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.
# The digits are stored in reverse order, e.g. the number 321 is represented as 1 -> 2 -> 3 -> in the linked list.
# Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Return the sum of the two numbers as a linked list.

# Example 1:
# Input: l1 = [1,2,3], l2 = [4,5,6]
# Output: [5,7,9]
# Explanation: 321 + 654 = 975.

# Example 2:
# Input: l1 = [9], l2 = [9]
# Output: [8,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if val1 else 0 
            val2 = l2.val if val2 else 0 

            sum = val1 + val2 + carry 
            rem = sum % 10 
            carry = sum // 10 
            cur.next = ListNode(rem)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next


#########################################################################################

# Find the Duplicate Number
# Medium
# You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.
# Every integer appears exactly once, except for one integer which appears two or more times. Return the integer that appears more than once.

# Example 1:
# Input: nums = [1,2,3,2,2]
# Output: 2

# Example 2:
# Input: nums = [1,2,3,4,4]
# Output: 4
# Follow-up: Can you solve the problem without modifying the array nums and using O(1) extra space?

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow 



#########################################################################################

# LRU Cache
# Medium
# Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

# LRUCache(int capacity) Initialize the LRU cache of size capacity.
# int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
# A key is considered used if a get or a put operation is called on it.

# Ensure that get and put each run in O(1) average time complexity.

# Example 1:
# Input:
# ["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]
# Output:
# [null, null, 10, null, null, 20, -1]

# Explanation:
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 10);  // cache: {1=10}
# lRUCache.get(1);      // return 10
# lRUCache.put(2, 20);  // cache: {1=10, 2=20}
# lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
# lRUCache.get(2);      // returns 20 
# lRUCache.get(1);      // return -1 (not found)

class LRUCache:

    def __init__(self, capacity: int):
        

    def get(self, key: int) -> int:
        

    def put(self, key: int, value: int) -> None:
        

#########################################################################################
# Merge K Sorted Linked Lists
# Hard
# You are given an array of k linked lists lists, where each list is sorted in ascending order.
# Return the sorted linked list that is the result of merging all of the individual linked lists.

# Example 1:
# Input: lists = [[1,2,4],[1,3,5],[3,6]]
# Output: [1,1,2,3,3,4,5,6]

# Example 2:
# Input: lists = []
# Output: []

# Example 3:
# Input: lists = [[]]
# Output: []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
#########################################################################################
# Reverse Nodes in K-Group
# Hard
# You are given the head of a singly linked list head and a positive integer k.
# You must reverse the first k nodes in the linked list, and then reverse the next k nodes, and so on. If there are fewer than k nodes left, leave the nodes as they are.
# Return the modified list after reversing the nodes in each group of k.
# You are only allowed to modify the nodes' next pointers, not the values of the nodes.

# Example 1:
# Input: head = [1,2,3,4,5,6], k = 3
# Output: [3,2,1,6,5,4]

# Example 2:
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        