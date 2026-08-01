"""
LeetCode 387 - First Unique Character in a String

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)
"""

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = [0] * 26

        for char in s:
            index = ord(char) - ord("a")
            count[index] += 1

        for i, char in enumerate(s):
            index = ord(char) - ord("a")
            if count[index] == 1:
                return i

        return -1
