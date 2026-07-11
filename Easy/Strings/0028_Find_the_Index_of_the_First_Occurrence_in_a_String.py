"""
LeetCode 28 - Find the Index of the First Occurrence in a String

Difficulty: Easy

Time Complexity: O((n - m + 1) x m)
Space Complexity: O(1)
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_length = len(needle)
        haystack_length = len(haystack)
        
        for i in range(haystack_length - needle_length + 1):
            for j in range(needle_length):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i
        return -1
