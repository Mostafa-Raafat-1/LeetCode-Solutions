"""--------------Recursion--------------"""

"""
LeetCode 509 - Fibonacci Number

Difficulty: Easy

Time Complexity: O(2^n)
Space Complexity: O(n)

Technique:
- Recursion
"""
# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             return self.fib(n - 1) + self.fib(n - 2)


"""--------------Iterative--------------"""

"""
LeetCode 509 - Fibonacci Number

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Technique:
- Iteration
"""


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        first, second = 0, 1

        for _ in range(2, n + 1):
            first, second = second, first + second

        return second


print(Solution().fib(5))
