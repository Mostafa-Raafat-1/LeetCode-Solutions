from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
LeetCode 226 - Invert Binary Tree

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(w)

Technique:
- Breadth-First Search (BFS)
- Queue
"""


# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if root:
#             queue = deque([root])
#         else:
#             return None

#         while queue:
#             node = queue.popleft()
#             node.right, node.left = node.left, node.right
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)

#         return root


"""
LeetCode 226 - Invert Binary Tree

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(h)

Technique:
- Depth-First Search (DFS)
- Recursion
"""


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        self.invertTree(root.left)
        self.invertTree(root.right)

        root.right, root.left = root.left, root.right

        return root


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
Solution().invertTree(root)
