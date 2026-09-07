"""
LeetCode 752 - Open the Lock

Difficulty: Medium

Time Complexity: O(10^4)
Space Complexity: O(10^4)

Technique:

* Breadth-First Search (BFS)
"""

from typing import List
from collections import deque


class Solution:
    def _get_neighbors(self, number):
        neighbors = []

        for i, digit in enumerate(number):
            digit = int(digit)

            low = (digit - 1) % 10
            high = (digit + 1) % 10

            neighbors.append(number[:i] + str(low) + number[i + 1 :])
            neighbors.append(number[:i] + str(high) + number[i + 1 :])

        return neighbors

    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0

        deadends = set(deadends)
        if "0000" in deadends:
            return -1

        queue = deque(["0000"])
        visited = {"0000"}
        turns = 0

        while queue:
            for _ in range(len(queue)):
                number = queue.popleft()
                neighbors = self._get_neighbors(number)

                for neighbor in neighbors:
                    if neighbor == target:
                        return turns + 1
                    if neighbor not in visited and neighbor not in deadends:
                        visited.add(neighbor)
                        queue.append(neighbor)
            turns += 1
        return -1


print(
    Solution().openLock(
        deadends=["0201", "0101", "0102", "1212", "2002"], target="0202"
    )
)
