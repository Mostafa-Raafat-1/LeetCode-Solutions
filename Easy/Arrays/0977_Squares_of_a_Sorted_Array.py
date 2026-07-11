"""
LeetCode 977 - Squares of a Sorted Array

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Technique:
- Two Pointers
"""


from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        temp = []
        new_list = []
        
        while left <= right:
            left_number = abs(nums[left])
            right_number = abs(nums[right])
            
            if left_number > right_number:
                temp.append(nums[left])
                left +=1
            else:
                temp.append(nums[right])
                right -=1
        
        for number in reversed(temp):
            new_list.append(number**2)
        
        return new_list

solution = Solution()
result = solution.sortedSquares(nums=[-10000, 10000])
print(result)