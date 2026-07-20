"""
LeetCode 167 - Two Sum II - Input Array Is Sorted

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(1)

Technique:
- Two Pointers
"""


from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while right > left:
            total = numbers[left] + numbers[right]
            
            if total > target:
                right -=1
            elif total < target:
                left +=1
            else:
                return [left + 1, right + 1]