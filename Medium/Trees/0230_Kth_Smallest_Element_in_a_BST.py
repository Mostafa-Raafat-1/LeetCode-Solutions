from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
LeetCode 230 - Kth Smallest Element in a BST

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(H)

Technique:
- Recursive Inorder Traversal
"""
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         current = 0
#         smallest = 0

#         def get_element(node, k):
#             nonlocal smallest, current
#             if not node:
#                 return

#             get_element(node.left, k)
#             current += 1
#             if current == k:
#                 smallest = node.val
#                 return
#             get_element(node.right, k)

#         get_element(root, k)
#         return smallest


"""
LeetCode 230 - Kth Smallest Element in a BST

Difficulty: Medium

Time Complexity: O(H + k)
Space Complexity: O(H)

Technique:
- Recursive Inorder Traversal
"""
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         def inorder(node):
#             nonlocal k

#             if not node:
#                 return

#             result = inorder(node.left)
#             if result is not None:
#                 return result

#             k -= 1
#             if k == 0:
#                 return node.val

#             return inorder(node.right)

#         return inorder(root)


"""
LeetCode 230 - Kth Smallest Element in a BST

Difficulty: Medium

Time Complexity: O(H + k)
Space Complexity: O(H)

Technique:
- Iterative Inorder Traversal
"""


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current = root
        stack = []

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            k -= 1
            if k == 0:
                return current.val

            current = current.right
