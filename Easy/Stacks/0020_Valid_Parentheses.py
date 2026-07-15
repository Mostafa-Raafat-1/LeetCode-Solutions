"""
LeetCode 20 - Valid Parentheses

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Technique:
- Stack
"""


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for bracket in s:
            if bracket not in pairs:
                stack.append(bracket)
                continue

            if not stack or stack.pop() != pairs[bracket]:
                return False

        return not stack