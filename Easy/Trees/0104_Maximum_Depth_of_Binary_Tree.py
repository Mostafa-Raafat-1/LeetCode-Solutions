"""
LeetCode 104 - Maximum Depth of Binary Tree

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(h)

Technique:
- Recursion
- Depth-First Search (DFS)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left) if root.left else 0
        right = self.maxDepth(root.right) if root.right else 0

        return max(left, right) + 1
