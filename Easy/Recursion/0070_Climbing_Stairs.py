"""
LeetCode 70 - Climbing Stairs

Difficulty: Easy

Time Complexity: O(2^n)
Space Complexity: O(n)

Technique:
- Recursion
"""

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 1 or n == 2:
#             return n

#         return self.climbStairs(n - 1) + self.climbStairs(n - 2)


"""
LeetCode 70 - Climbing Stairs

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Technique:
- Iterative
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n

        first = 1
        second = 2

        for _ in range(3, n + 1):
            first, second = second, first + second

        return second


print(Solution().climbStairs(6))
