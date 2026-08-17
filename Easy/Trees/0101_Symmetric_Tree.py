from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
LeetCode 101 - Symmetric Tree

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(h)

Technique:
- Recursion
- DFS
"""


# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True

#         def is_mirror(left, right):
#             if not left and not right:
#                 return True
#             if not left or not right:
#                 return False
#             return (
#                 left.val == right.val
#                 and is_mirror(left.left, right.right)
#                 and is_mirror(left.right, right.left)
#             )

#         return is_mirror(root.left, root.right)


"""
LeetCode 101 - Symmetric Tree

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(w)

Technique:
- BFS
- Queue
"""


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([(root.left, root.right)])

        while queue:
            left, right = queue.popleft()

            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False

            queue.append((left.left, right.right))
            queue.append((left.right, right.left))

        return True


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(Solution().isSymmetric(root))
