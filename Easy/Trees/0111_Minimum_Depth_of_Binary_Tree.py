"""
LeetCode 111 - Minimum Depth of Binary Tree

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Technique:
- Breadth-First Search (BFS)
"""

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if not node.right and not node.left:
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))


"""
LeetCode 111 - Minimum Depth of Binary Tree

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(h)

Technique:
- Depth-First Search (DFS)
- Recursion
"""

# class Solution:
#     def minDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         if not root.left:
#             return 1 + self.minDepth(root.right)

#         if not root.right:
#             return 1 + self.minDepth(root.left)

#         return 1 + min(
#             self.minDepth(root.left),
#             self.minDepth(root.right)
#         )
