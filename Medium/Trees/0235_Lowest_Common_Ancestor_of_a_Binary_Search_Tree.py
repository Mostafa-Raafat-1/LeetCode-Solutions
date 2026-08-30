class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
LeetCode 235 - Lowest Common Ancestor of a Binary Search Tree

Difficulty: Medium

Time Complexity: O(h)
Space Complexity: O(h)

Technique:
- Recursion
"""
# class Solution:
#     def lowestCommonAncestor(
#         self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
#     ) -> "TreeNode":
#         if p.val > root.val and q.val > root.val:
#             return self.lowestCommonAncestor(root.right, p, q)

#         if p.val < root.val and q.val < root.val:
#             return self.lowestCommonAncestor(root.left, p, q)

#         return root


"""
LeetCode 235 - Lowest Common Ancestor of a Binary Search Tree

Difficulty: Medium

Time Complexity: O(h)
Space Complexity: O(1)

Technique:
- Iteration
"""


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root
