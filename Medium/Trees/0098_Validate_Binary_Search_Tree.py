"""
LeetCode 98 - Validate Binary Search Tree

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(h)

Technique:
- DFS with Bounds
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if not node:
                return True

            return (
                low < node.val < high
                and validate(node.left, low, node.val)
                and validate(node.right, node.val, high)
            )

        return validate(root, float("-inf"), float("inf"))
