"""
LeetCode 66 - Plus One

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)
"""


from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:    
        i = len(digits) - 1
        
        while i >=0:
            if digits[i] < 9:
                digits[i] +=1
                return digits
            
            digits[i] = 0
            i -=1
            
        return [1] + digits

solution = Solution()
result = solution.plusOne(digits = [1,2,9])
print(result)