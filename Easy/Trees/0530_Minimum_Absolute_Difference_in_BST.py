"""
LeetCode 530 - Minimum Absolute Difference in BST

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(h)

Technique:
- Inorder Traversal
- Track Previous Value
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        previous = None
        min_difference = float("inf")

        def get_difference(node):
            nonlocal previous, min_difference

            if not node:
                return

            get_difference(node.left)

            if previous is not None:
                min_difference = min(min_difference, node.val - previous)

            previous = node.val

            get_difference(node.right)

        get_difference(root)
        return min_difference
