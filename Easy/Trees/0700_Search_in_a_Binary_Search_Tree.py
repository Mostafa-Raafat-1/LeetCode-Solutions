from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""------------ Recursive ------------"""
"""
LeetCode 700 - Search in a Binary Search Tree

Difficulty: Easy

Time Complexity: O(h)
Space Complexity: O(h)

Technique:
- Binary Search Tree
- Recursion
"""
# class Solution:
#     def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         if not root:
#             return None

#         if val == root.val:
#             return root
#         elif val > root.val:
#             return self.searchBST(root.right, val)
#         else:
#             return self.searchBST(root.left, val)


"""------------ Iterative ------------"""
"""
LeetCode 700 - Search in a Binary Search Tree

Difficulty: Easy

Time Complexity: O(h)
Space Complexity: O(1)

Technique:
- Binary Search Tree
- Iteration
"""


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        while node:
            if val == node.val:
                return node
            elif val > node.val:
                node = node.right
                continue
            else:
                node = node.left

        return None
