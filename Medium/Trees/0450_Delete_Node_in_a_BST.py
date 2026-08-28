"""
LeetCode 450 - Delete Node in a BST

Difficulty: Medium

Time Complexity: O(h)
Space Complexity: O(h)

Technique:
- Recursion
- Inorder Predecessor
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder_predecessor(self, node):
        if not node:
            return

        if node.right:
            return self.inorder_predecessor(node.right)
        return node.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return

        if root.val == key:
            if not root.left and not root.right:
                return
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            root.val = self.inorder_predecessor(root.left)
            root.left = self.deleteNode(root.left, root.val)
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root
