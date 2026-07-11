"""
LeetCode 1672 - Richest Customer Wealth

Difficulty: Easy

Time Complexity: O(n x m)
Space Complexity: O(1)
"""


from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        
        for customer in accounts: # => n
            customer_wealth = sum(customer) # => n * m
            max_wealth = max(customer_wealth, max_wealth)
        
        return max_wealth