"""
LeetCode 9 - Palindrome Number

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        number = str(x)
        
        for i in range(len(number) // 2):
            if number[i] != number[-1 - i]:
                return False
        return True