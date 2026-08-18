"""
LeetCode 103 - Binary Tree Zigzag Level Order Traversal

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(n)

Technique:
- Breadth-First Search (BFS)
- Queue
"""

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True
        while queue:
            level_size = len(queue)
            level = [None for _ in range(level_size)]
            for i in range(level_size):
                node = queue.popleft()
                index = i if left_to_right else -1 - i
                level[index] = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)
            left_to_right = not left_to_right
        return result


# Level 0
root = TreeNode(1)

# Level 1
root.left = TreeNode(2)
root.right = TreeNode(3)

# Level 2
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Level 3
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)

root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(11)

root.right.left.left = TreeNode(12)
root.right.left.right = TreeNode(13)

root.right.right.left = TreeNode(14)
root.right.right.right = TreeNode(15)

# Level 4
root.left.left.left.left = TreeNode(16)
root.left.left.left.right = TreeNode(17)

root.left.left.right.left = TreeNode(18)
root.left.left.right.right = TreeNode(19)

root.left.right.left.left = TreeNode(20)
root.left.right.left.right = TreeNode(21)

root.left.right.right.left = TreeNode(22)
root.left.right.right.right = TreeNode(23)

root.right.left.left.left = TreeNode(24)
root.right.left.left.right = TreeNode(25)

root.right.left.right.left = TreeNode(26)
root.right.left.right.right = TreeNode(27)

root.right.right.left.left = TreeNode(28)
root.right.right.left.right = TreeNode(29)

root.right.right.right.left = TreeNode(30)
root.right.right.right.right = TreeNode(31)

print(Solution().zigzagLevelOrder(root))
