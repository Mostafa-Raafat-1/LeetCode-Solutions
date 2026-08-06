"""------------------ Recursion ------------------"""

"""
LeetCode 326 - Power of Three

Difficulty: Easy

Time Complexity: O(log₃ n)
Space Complexity: O(log₃ n)

Technique:
- Recursion
"""
# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         if n == 1:
#             return True
#         if n < 1 or n % 3 != 0:
#             return False

#         return self.isPowerOfThree(n // 3)


"""
LeetCode 326 - Power of Three

Difficulty: Easy

Time Complexity: O(log₃ n)
Space Complexity: O(1)

Technique:
- Iteration
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        while n > 1:
            if n % 3 != 0:
                return False
            n //= 3
        return True
