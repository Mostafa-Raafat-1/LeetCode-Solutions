"""
LeetCode 3992 - Rearrange String to Avoid Character Pair

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        ys = []
        rest = []
        for char in s:
            if char == y:
                ys.append(char)
            else:
                rest.append(char)
        return "".join(ys) + "".join(rest)
