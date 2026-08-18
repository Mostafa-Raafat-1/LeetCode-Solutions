"""
LeetCode 102 - Binary Tree Level Order Traversal

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(n)

Technique:
- Breadth-First Search (BFS)
- Queue
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque()
        if root:
            queue.append(root)

        while queue:
            level = []
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)

        return result
