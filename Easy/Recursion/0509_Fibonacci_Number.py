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
# class Solution:
#     def fib(self, n: int) -> int:
#         if n <= 1:
#             return n

#         first, second = 0, 1

#         for _ in range(2, n + 1):
#             first, second = second, first + second

#         return second


"""
LeetCode 509 - Fibonacci Number

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Technique:
- Recursion
- Top-Down Dynamic Programming (Memoization)
"""
# class Solution:
#     def fib(self, n: int) -> int:
#         def fibonacci(n, memo):
#             if n in memo:
#                 return memo[n]

#             if n <= 1:
#                 return n

#             result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

#             memo[n] = result

#             return result

#         return fibonacci(n, {})


"""
LeetCode 509 - Fibonacci Number

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(n)

Technique:
- Recursion
- Top-Down Dynamic Programming (Memoization)
- functools.lru_cache
"""
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        return self.fib(n - 1) + self.fib(n - 2)
