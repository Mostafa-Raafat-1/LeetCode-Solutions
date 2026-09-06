"""
LeetCode 547 - Number of Provinces

Difficulty: Medium

Time Complexity: O(n²)
Space Complexity: O(n)

Technique:
- Breadth-First Search (BFS)
"""

from typing import List
from collections import deque


class Solution:
    def _retrieve_neighbors(self, isConnected, index):
        neighbors = []

        for i, val in enumerate(isConnected[index]):
            if val == 1 and i != index:
                neighbors.append(i)

        return neighbors

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = set()
        queue = deque()

        for city in range(len(isConnected)):
            if city in visited:
                continue

            queue.append(city)
            visited.add(city)

            while queue:
                index = queue.popleft()
                neighbors = self._retrieve_neighbors(isConnected, index)

                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

            provinces += 1

        return provinces
