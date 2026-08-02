"""
LeetCode 202 - Happy Number

Difficulty: Easy

Time Complexity: O(log n)
Space Complexity: O(1)

Technique:
- Floyd's Cycle Detection (Tortoise and Hare)
- Fast & Slow Pointers
"""


class Solution:
    def next_number(self, n):
        total = 0
        while n:
            digit = n % 10
            total += digit * digit
            n //= 10

        return total

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n

        while True:
            slow = self.next_number(slow)
            fast = self.next_number(self.next_number(fast))

            if slow == fast:
                break

        return slow == 1


"""
LeetCode 202 - Happy Number

Difficulty: Easy

Time Complexity: O(log n)
Space Complexity: O(1)

Technique:
- Cycle Detection
"""


class Solution:
    def next_number(self, n):
        total = 0
        while n:
            digit = n % 10
            total += digit * digit
            n //= 10

        return total

    def isHappy(self, n: int) -> bool:
        number = n
        seen = set()
        total = 0

        while number not in seen:
            seen.add(number)
            total = 0
            while number != 0:
                remainder = number % 10
                number //= 10
                total += remainder**2

            if total == 1:
                return True
            number = total

        return False
