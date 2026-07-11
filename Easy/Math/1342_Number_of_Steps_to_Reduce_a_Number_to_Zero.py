"""
LeetCode 1342 - Number of Steps to Reduce a Number to Zero

Difficulty: Easy

Time Complexity: O(log n)
Space Complexity: O(1)
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
            
        while num:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            
            steps +=1

        return steps