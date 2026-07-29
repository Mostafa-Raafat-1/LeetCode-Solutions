"""
LeetCode 290 - Word Pattern

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        pattern_to_s = {}
        s_to_pattern = {}

        if len(s_list) != len(pattern):
            return False

        for char, word in zip(pattern, s_list):
            if char in pattern_to_s:
                if pattern_to_s[char] != word:
                    return False
            else:
                pattern_to_s[char] = word

            if word in s_to_pattern:
                if s_to_pattern[word] != char:
                    return False
            else:
                s_to_pattern[word] = char

        return True
