"""
LeetCode 121 - Best Time to Buy and Sell Stock

Difficulty: Easy

Time Complexity: O(n)
Space Complexity: O(1)

Technique:
- Greedy
"""


from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                max_profit = max(prices[i] - min_price, max_profit)
        return max_profit

solution = Solution()
result = solution.maxProfit(prices=[7, 1, 5, 3, 6, 4])
print(result)