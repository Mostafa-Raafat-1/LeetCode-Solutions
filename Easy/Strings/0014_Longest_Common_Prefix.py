"""
LeetCode 14 - Longest Common Prefix

Difficulty: Easy

Time Complexity: O(n * m)
Space Complexity: O(m)
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(1, len(strs)):
            string = strs[i]
            j = 0

            while j < len(prefix) and j < len(string):
                if prefix[j] != string[j]:
                    break
                j += 1

            prefix = prefix[:j]

            if not prefix:
                return ""

        return prefix
