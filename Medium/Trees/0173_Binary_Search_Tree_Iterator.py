"""
LeetCode 173 - Binary Search Tree Iterator

Difficulty: Medium

__init__():
    Time Complexity: O(h)
    Space Complexity: O(h)

_inorder():
    Time Complexity: O(h)
    Space Complexity: O(h)  # recursion stack

next():
    Time Complexity: O(h) worst case, O(1) amortized
    Space Complexity: O(h)

hasNext():
    Time Complexity: O(1)
    Space Complexity: O(1)

Technique:
- In-Order Traversal
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._inorder(root)

    def _inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        self._inorder(node.right)
        return node.val

    def hasNext(self) -> bool:
        return bool(self.stack)
