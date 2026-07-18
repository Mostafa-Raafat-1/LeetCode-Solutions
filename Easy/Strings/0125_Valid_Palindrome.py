"""
LeetCode 125 - Valid Palindrome

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Technique:
- Two Pointers
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        right = len(s) - 1
        left = 0
        
        while right > left:
            if not s[right].isalnum():
                right -=1
                continue
            elif not s[left].isalnum():
                left +=1
                continue
            
            if s[right].lower() != s[left].lower():
                return False
            
            left +=1
            right -=1

        return True