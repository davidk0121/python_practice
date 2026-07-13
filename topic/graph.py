
# Number of Islands
# Medium
# Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

# An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).

# Example 1:
# Input: grid = [
#     ["0","1","1","1","0"],
#     ["0","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
#   ]
# Output: 1

# Example 2:
# Input: grid = [
#     ["1","1","0","0","1"],
#     ["1","1","0","0","1"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
#   ]
# Output: 4

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

#########################################################################################

# Max Area of Island
# Medium
# Topics
# Company Tags
# Hints
# You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).
# An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges 
# of the grid are surrounded by water.

# The area of an island is defined as the number of cells within the island.
# Return the maximum area of an island in grid. If no island exists, return 0.

# Example 1:
# Input: grid = [
#   [0,1,1,0,1],
#   [1,0,1,0,1],
#   [0,1,1,0,1],
#   [0,1,0,0,1]
# ]
# Output: 6
# Explanation: 1's cannot be connected diagonally, so the maximum area of the island is 6.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

#########################################################################################

# Clone Graph
# Medium
# Given a node in a connected undirected graph, return a deep copy of the graph.
# Each node in the graph contains an integer value and a list of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
# The graph is shown in the test cases as an adjacency list. An adjacency list is a mapping of nodes to lists, 
# used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

# For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph. 
# The index of each node within the adjacency list is the same as the node's value (1-indexed).

# The input node will always be the first node in the graph and have 1 as the value.

# Example 1:
# Input: adjList = [[2],[1,3],[2]]
# Output: [[2],[1,3],[2]]
# Explanation: There are 3 nodes in the graph.
# Node 1: val = 1 and neighbors = [2].
# Node 2: val = 2 and neighbors = [1, 3].
# Node 3: val = 3 and neighbors = [2].

# Example 2:
# Input: adjList = [[]]
# Output: [[]]
# Explanation: The graph has one node with no neighbors.

# Example 3:
# Input: adjList = []
# Output: []
# Explanation: The graph is empty.

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

#########################################################################################
# Islands and Treasure
# Medium
# You are given a 
# m
# ×
# n
# m×n 2D grid initialized with these three possible values:

# -1 - A water cell that can not be traversed.
# 0 - A treasure chest.
# INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
# Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a 
# treasure chest then the value should remain INF.

# Assume the grid can only be traversed up, down, left, or right.

# Modify the grid in-place.

# Example 1:
# Input: [
#   [2147483647,-1,0,2147483647],
#   [2147483647,2147483647,2147483647,-1],
#   [2147483647,-1,2147483647,-1],
#   [0,-1,2147483647,2147483647]
# ]
# Output: [
#   [3,-1,0,1],
#   [2,2,1,-1],
#   [1,-1,2,-1],
#   [0,-1,3,4]
# ]


# Example 2:
# Input: [
#   [0,-1],
#   [2147483647,2147483647]
# ]
# Output: [
#   [0,-1],
#   [1,2]
# ]

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        

#########################################################################################

# Rotting Fruit
# Medium
# You are given a 2-D matrix grid. Each cell can have one of three possible values:

# 0 representing an empty cell
# 1 representing a fresh fruit
# 2 representing a rotten fruit
# Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit 
# also becomes rotten.

# Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state 
# is impossible within the grid, return -1.

# Example 1:
# Input: grid = [[1,1,0],[0,1,1],[0,1,2]]
# Output: 4

# Example 2:
# Input: grid = [[1,0,1],[0,2,0],[1,0,1]]
# Output: -1

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
#########################################################################################

# Pacific Atlantic Water Flow
# Medium
# You are given a rectangular island heights where heights[r][c] represents the height above sea 
# level of the cell at coordinate (r, c).

# The islands borders the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean from the 
# bottom and right sides.

# Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell with height 
# equal or lower. Water can also flow into the ocean from cells adjacent to the ocean.

# Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans. Return it as a 
# 2D list where each element is a list [r, c] representing the row and column of the cell. You may return the answer in any order.

# Example 1:
# Input: heights = [
#   [4,2,7,3,4],
#   [7,4,6,4,7],
#   [6,3,5,3,6]
# ]
# Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]

# Example 2:
# Input: heights = [[1],[1]]
# Output: [[0,0],[1,0]]

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

#########################################################################################

# Surrounded Regions
# Medium
# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell. Regions can have any shape; they do not need to be squares 
# or rectangles.
# Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such 
# regions are completely enclosed by 'X' cells.
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need 
# to return anything.

# Example 1:
# Input: board = [
#   ["X","X","X","X"],
#   ["X","O","O","X"],
#   ["X","X","O","X"],
#   ["X","O","X","X"]
# ]

# Output: [
#   ["X","X","X","X"],
#   ["X","X","X","X"],
#   ["X","X","X","X"],
#   ["X","O","X","X"]
# ]
# Explanation: The bottom 'O' region is not captured because it touches the edge of the board, so it cannot be surrounded.


# Example 2:
# Input: board = [["X"]]
# Output: [["X"]]

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        

#########################################################################################
# Course Schedule
# Medium
# You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b 
# first if you want to take course a.

# The pair [0, 1], indicates that must take course 1 before taking course 0.

# There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

# Return true if it is possible to finish all courses, otherwise return false.

# Example 1:
# Input: numCourses = 2, prerequisites = [[0,1]]
# Output: true
# Explanation: First take course 1 (no prerequisites) and then take course 0.

# Example 2:
# Input: numCourses = 2, prerequisites = [[0,1],[1,0]]
# Output: false
# Explanation: In order to take course 1 you must take course 0, and to take course 0 you must take course 1. 
# So it is impossible.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
#########################################################################################
# Course Schedule II
# Medium
# You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b 
# first if you want to take course a.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

# Return a valid ordering of courses you can take to finish all courses. If there are many valid answers, return 
# any of them. If it's not possible to finish all courses, return an empty array.

# Example 1:
# Input: numCourses = 3, prerequisites = [[1,0]]
# Output: [0,1,2]
# Explanation: We must ensure that course 0 is taken before course 1.

# Example 2:
# Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]
# Output: []
# Explanation: It's impossible to finish all courses.


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
#########################################################################################
# Graph Valid Tree
# Medium
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
# write a function to check whether these edges make up a valid tree.

# Example 1:
# Input:
# n = 5
# edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# Output:
# true

# Example 2:
# Input:
# n = 5
# edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
# Output:
# false
# Note:

# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the 
# same as [1, 0] and thus will not appear together in edges.

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
#########################################################################################

# Number of Connected Components in an Undirected Graph
# Medium
# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [aᵢ, bᵢ] indicates 
# that there is an edge between aᵢ and bᵢ in the graph.

# Return the number of connected components in the graph.

# Example 1:
# Input:
# n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2

# Example 2:
# Input:
# n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]

# Output: 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

#########################################################################################

# Redundant Connection
# Medium
# You are given a connected undirected graph with n nodes labeled from 1 to n. Initially, it contained 
# no cycles and consisted of n-1 edges.

# We have now added one additional edge to the graph. The edge has two different vertices chosen from 1 to n, 
# and was not an edge that previously existed in the graph.

# The graph is represented as an array edges of length n where edges[i] = [ai, bi] represents an edge between 
# nodes ai and bi in the graph.

# Return an edge that can be removed so that the graph is still a connected non-cyclical graph. If there are 
# multiple answers, return the edge that appears last in the input edges.

# Example 1:
# Input: edges = [[1,2],[1,3],[3,4],[2,4]]
# Output: [2,4]

# Example 2:
# Input: edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
# Output: [3,4]

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        

