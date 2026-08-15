"""
LeetCode 144 - Binary Tree Preorder Traversal

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(h)

Technique:
- Depth-First Search (DFS)
- Recursion
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def preorder(node):
            if not node:
                return

            result.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return result
