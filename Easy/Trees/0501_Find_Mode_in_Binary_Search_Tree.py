"""
LeetCode 501 - Find Mode in Binary Search Tree

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(h) excluding output
                  O(1) excluding output and recursion stack

Technique:
- Inorder Traversal
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        max_frequency = 0
        current_frequency = 0
        current_value = None
        modes = []

        def inorder(node):
            nonlocal max_frequency, current_frequency
            nonlocal current_value, modes

            if not node:
                return

            inorder(node.left)

            if node.val == current_value:
                current_frequency += 1
            else:
                current_value = node.val
                current_frequency = 1

            if current_frequency > max_frequency:
                max_frequency = current_frequency
                modes = [node.val]
            elif current_frequency == max_frequency:
                modes.append(node.val)

            inorder(node.right)

        inorder(root)
        return modes
