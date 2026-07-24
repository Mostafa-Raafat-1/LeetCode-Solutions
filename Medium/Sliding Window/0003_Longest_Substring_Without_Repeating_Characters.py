"""
3. Longest Substring Without Repeating Characters

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(n)

Technique:
- Sliding Window
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        window = set(s[0])
        longest = 1
        left = 0
        right = 1

        while right < len(s):
            if not s[right] in window:
                window.add(s[right])
                right += 1
            else:
                while s[left] != s[right]:
                    window.remove(s[left])
                    left += 1

                left += 1
                right += 1

            longest = max(longest, right - left)

        return longest


# ChatGpt's Solution:
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         window = set()
#         left = 0
#         longest = 0

#         for right in range(len(s)):
#             while s[right] in window:
#                 window.remove(s[left])
#                 left += 1

#             window.add(s[right])
#             longest = max(longest, right - left + 1)

#         return longest
