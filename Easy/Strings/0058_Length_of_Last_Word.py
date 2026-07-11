"""
LeetCode 58 - Length of Last Word

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        words=s.split(" ")
        return len(words[-1])