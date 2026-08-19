"""
LeetCode 113 - Path Sum II

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(h)

Technique:
- DFS
- Backtracking
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def path(node: TreeNode, total: int, items: list):
            if not node:
                return

            items.append(node.val)
            total += node.val
            path(node.left, total, items)
            path(node.right, total, items)

            if not node.right and not node.left and total == targetSum:
                result.append(items.copy())

            items.pop()

        path(root, 0, [])
        return result
