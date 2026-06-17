
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
        self.maxD = 0
        def dfs(cur):
            if not cur: return 0
            left = dfs(cur.left)
            right = dfs(cur.right) 
            self.maxD = max(self.maxD, left + right)
            return 1 + max(left, right)    

        dfs(root)
        return self.maxD

#########################################################################################
# Balanced Binary Tree
# Easy
# Given a binary tree, return true if it is height-balanced and false otherwise.
# A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Example 1:
# Input: root = [1,2,3,null,null,4]
# Output: true

# Example 2:
# Input: root = [1,2,3,null,null,4,null,5]
# Output: false

# Example 3:
# Input: root = []
# Output: true

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(cur):
            if not cur: return [True, 0]
            left = dfs(cur.left)
            right = dfs(cur.right)

            balanced = (abs(left[1] - right[1]) <= 1) and left[0] and right[0] 
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]

#########################################################################################
# Same Binary Tree
# Easy
# Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.
# Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [4,7], q = [4,null,7]
# Output: false

# Example 3:
# Input: p = [1,2,3], q = [1,3,2]
# Output: false

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

#########################################################################################
# Subtree of Another Tree
# Easy
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Example 1:
# Input: root = [1,2,3,4,5], subRoot = [2,4,5]
# Output: true

# Example 2:
# Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]
# Output: false

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        if not subRoot: return True

        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
#########################################################################################
# Lowest Common Ancestor in Binary Search Tree
# Medium
# Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.
# The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants. The ancestor is allowed to be a descendant of itself.

# Example 1:
# Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8
# Output: 5

# Example 2:
# Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4
# Output: 3

# Explanation: The LCA of nodes 3 and 4 is 3, since a node can be a descendant of itself.

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur.val
        
#########################################################################################
# Binary Tree Level Order Traversal
# Medium
# Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

# Example 1:
# Input: root = [1,2,3,4,5,6,7]
# Output: [[1],[2,3],[4,5,6,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque([root])

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    level.append(node.val)
            if level:
                res.append(level)
        return res

#########################################################################################
# Binary Tree Right Side View
# Medium
# You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.

# Example 1:
# Input: root = [1,2,3,null,4,null,5]
# Output: [1,3,5]

# Example 2:
# Input: root = [1,2,3,4,null,null,null,5]
# Output: [1,3,4,5]

# Example 3:
# Input: root = [1,null,2]
# Output: [1,2]

# Example 4:
# Input: root = []
# Output: []

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        
        return res
        
#########################################################################################
# Count Good Nodes in Binary Tree
# Medium
# Within a binary tree, a node x is considered good if the path from the root of the tree to the node x contains no nodes with a value greater than the value of node x
# Given the root of a binary tree root, return the number of good nodes within the tree.

# Example 1:
# Input: root = [2,1,1,3,null,1,5]
# Output: 3

# Example 2:
# Input: root = [1,2,-1,3,4]
# Output: 4

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, maxVal):
            if not node:
                return 0
            
            res = 1 if node.val >= maxVal else 0 
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)
        

#########################################################################################
# Valid Binary Search Tree
# Medium
# Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.
# A valid binary search tree satisfies the following constraints:

# The left subtree of every node contains only nodes with keys less than the node's key.
# The right subtree of every node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees are also binary search trees.

# Example 1:
# Input: root = [2,1,3]
# Output: true

# Example 2:
# Input: root = [1,2,3]
# Output: false
# Explanation: The root node's value is 1 but its left child's value is 2 which is greater than 1.

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, left, right):
            if not node: return True
            if not (node.val > left and node.val < right):
                return False
            
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        return valid(root, float("-inf"), float("inf"))

#########################################################################################
# Kth Smallest Integer in BST
# Medium
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.
# A binary search tree satisfies the following constraints:
# The left subtree of every node contains only nodes with keys less than the node's key.
# The right subtree of every node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees are also binary search trees.

# Example 1:
# Input: root = [2,1,3], k = 1
# Output: 1

# Example 2:
# Input: root = [4,3,5,2,null], k = 4
# Output: 5

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        while cur or stack:
            # load in the stack
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right

#########################################################################################
# Construct Binary Tree from Preorder and Inorder Traversal
# Medium
# You are given two integer arrays preorder and inorder.
# preorder is the preorder traversal of a binary tree
# inorder is the inorder traversal of the same tree
# Both arrays are of the same size and consist of unique values.
# Rebuild the binary tree from the preorder and inorder traversals and return its root.

# Example 1:
# Input: preorder = [1,2,3,4], inorder = [2,1,3,4]
# Output: [1,2,3,null,null,null,4]

# Example 2:
# Input: preorder = [1], inorder = [1]
# Output: [1]

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not (preorder or inorder): return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root  

#########################################################################################

#########################################################################################

#########################################################################################

#########################################################################################