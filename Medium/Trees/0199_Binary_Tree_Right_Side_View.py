from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
LeetCode 199 - Binary Tree Right Side View

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(w)

Technique:
- BFS
- Level-Order Traversal
"""
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []

#         result = []
#         queue = deque([root])
#         while queue:
#             node = queue[-1]
#             result.append(node.val)
#             for _ in range(len(queue)):
#                 node = queue.popleft()
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#         return result


"""
LeetCode 199 - Binary Tree Right Side View

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(h)

Technique:
- DFS
- Recursion
"""


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def rightView(node, depth):
            if not node:
                return

            if depth >= len(result):
                result.append(node.val)

            rightView(node.right, depth + 1)
            rightView(node.left, depth + 1)

        rightView(root, 0)
        return result
