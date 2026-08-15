"""
LeetCode 145 - Binary Tree Postorder Traversal

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(h)

Technique:
- Depth-First Search (DFS)
- Recursion
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""-------------- Recursive --------------"""
# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         result = []

#         def postorder(node):
#             if not node:
#                 return

#             postorder(node.left)
#             postorder(node.right)
#             result.append(node.val)

#         postorder(root)
#         return result


"""-------------- Iterative --------------"""
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        node = root
        last_visited = None

        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]

                if node.right and node.right != last_visited:
                    node = node.right
                else:
                    result.append(node.val)
                    last_visited = node
                    stack.pop()
                    node = None

        return result
