"""
LeetCode 938 - Range Sum of BST

Difficulty: Easy

Time Complexity: O(n) worst case
Space Complexity: O(h)

Technique:
- BST Recursion
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
#         if not root:
#             return 0

#         if root.val < low:
#             return self.rangeSumBST(root.right, low, high)

#         if root.val > high:
#             return self.rangeSumBST(root.left, low, high)

#         return (
#             root.val
#             + self.rangeSumBST(root.left, low, high)
#             + self.rangeSumBST(root.right, low, high)
#         )


class Solution:
    def rangeSumBST(self, root, low, high):
        if not root:
            return 0

        if root.val < low:
            return self.rangeSumBST(root.right, low, high)

        if root.val > high:
            return self.rangeSumBST(root.left, low, high)

        if root.val == low:
            return root.val + self.rangeSumBST(root.right, low, high)

        if root.val == high:
            return root.val + self.rangeSumBST(root.left, low, high)

        return (
            root.val
            + self.rangeSumBST(root.left, low, high)
            + self.rangeSumBST(root.right, low, high)
        )
