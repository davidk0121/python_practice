
# Invert Binary Tree
# You are given the root of a binary tree root. Invert the binary tree and return its root.

# Example 1:
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,3,2,7,6,5,4]

# Example 2:
# Input: root = [3,2,1]
# Output: [3,1,2]

# Example 3:
# Input: root = []
# Output: []

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
    
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root

#########################################################################################
# Maximum Depth of Binary Tree
# Easy
# Given the root of a binary tree, return its depth.
# The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [1,2,3,null,null,4]
# Output: 3

# Example 2:
# Input: root = []
# Output: 0

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
#########################################################################################
# Diameter of Binary Tree
# The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.
# The length of a path between two nodes in a binary tree is the number of edges between the nodes. Note that the path can not include the same node twice.
# Given the root of a binary tree root, return the diameter of the tree.

# Example 1:
# Input: root = [1,null,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [1,2,3,5] or [5,3,2,4].

# Example 2:
# Input: root = [1,2,3]
# Output: 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        

#########################################################################################

#########################################################################################

#########################################################################################

#########################################################################################

#########################################################################################

#########################################################################################

#########################################################################################

#########################################################################################

#########################################################################################

#########################################################################################

#########################################################################################

#########################################################################################

#########################################################################################

#########################################################################################