"""
LeetCode 205 - Isomorphic Strings

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        opposites = {}

        for i, char in enumerate(s):
            opposite = opposites.get(char)

            if opposite and t[i] != opposite:
                return False

            opposites[char] = t[i]

        return True
