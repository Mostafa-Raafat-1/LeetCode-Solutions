"""
LeetCode 108 - Convert Sorted Array to Binary Search Tree

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(log n)

Technique:
- Divide and Conquer
- Recursion
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildBST(left, right):
            if left > right:
                return
            mid = (right + left) // 2
            node = TreeNode(nums[mid])
            node.left = buildBST(left, mid - 1)
            node.right = buildBST(mid + 1, right)
            return node

        return buildBST(0, len(nums) - 1)
