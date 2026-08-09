"""
LeetCode 50 - Pow(x, n)

Difficulty: Medium

Time Complexity: O(n)
Space Complexity: O(n)

Technique:

- Recursion
- Linear Recursive Multiplication
"""

# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n == 0:
#             return 1

#         elif n < 0:
#             return self.myPow(x, n + 1) * (1 / x)
#         else:
#             return self.myPow(x, n - 1) * x


"""
LeetCode 50 - Pow(x, n)

Difficulty: Medium

Time Complexity: O(log n)
Space Complexity: O(log n)

Technique:

- Recursion
- Exponentiation by Squaring
- Divide and Conquer
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == -1:
            return 1 / x

        remainder = n % 2
        return (self.myPow(x, n // 2) ** 2) * (x**remainder)
