"""
LeetCode 229 - Majority Element II

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(n)

Technique:
- Hash Map
"""


from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        repetitions = {}
        limit = len(nums) / 3
        result = []
        
        for number in nums:
            repetitions[number] = repetitions.get(number, 0) + 1
        
        for num, count in repetitions.items():
            if count > limit:
                result.append(num)
            
        return result
    
solution = Solution()
result = solution.majorityElement([1,2])
print(result)