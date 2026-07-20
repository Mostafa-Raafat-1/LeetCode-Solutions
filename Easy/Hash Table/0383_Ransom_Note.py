"""
LeetCode 383 - Ransom Note

Difficulty: Easy

Time Complexity: O(n + m)
Space Complexity: O(k)

Technique:
- Hash Map (Frequency Counting)
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_note_chars = {}
        magazine_chars = {}

        for char in ransomNote:
            count = ransom_note_chars.get(char, 0) + 1
            ransom_note_chars[char] = count

        for char in magazine:
            count = magazine_chars.get(char, 0) + 1
            magazine_chars[char] = count

        for char in ransom_note_chars:
            magazine_count = magazine_chars.get(char)
            if not magazine_count or magazine_count < ransom_note_chars[char]:
                return False

        return True
