from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
LeetCode 653 - Two Sum IV - Input is a BST

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Technique:
- DFS
- Hash Set
"""
# class Solution:
#     def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
#         elements = set()

#         def get_target(node, k):
#             if not node:
#                 return False

#             if k - node.val in elements:
#                 return True

#             elements.add(node.val)
#             return get_target(node.left, k) or get_target(node.right, k)

#         return get_target(root, k)


"""
LeetCode 653 - Two Sum IV - Input is a BST

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(h)

Technique:
- Two Pointers
- Iterative Inorder Traversal
"""


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        def push_left(node, stack):
            while node:
                stack.append(node)
                node = node.left

        def push_right(node, stack):
            while node:
                stack.append(node)
                node = node.right

        left_stack = []
        right_stack = []
        push_left(root, left_stack)
        push_right(root, right_stack)
        left = left_stack[-1].val
        right = right_stack[-1].val

        while left < right:
            total = right + left

            if total == k:
                return True

            if total < k:
                node = left_stack.pop()

                if node.right:
                    push_left(node.right, left_stack)

                left = left_stack[-1].val

            else:
                node = right_stack.pop()
                if node.left:
                    push_right(node.left, right_stack)

                right = right_stack[-1].val

        return False


root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.right = TreeNode(17)
root.right.right = TreeNode(20)

print(Solution().findTarget(root, 37))
