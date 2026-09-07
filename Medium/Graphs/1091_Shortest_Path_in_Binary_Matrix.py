"""
LeetCode 1091 - Shortest Path in Binary Matrix

Difficulty: Medium

Time Complexity: O(n²)
Space Complexity: O(n²)

Technique:
- Breadth-First Search (BFS)
"""

from typing import List
from collections import deque


class Solution:
    def _get_neighbors(self, i, j, size):
        neighbors = []
        directions = [
            (-1, -1),
            (1, 1),
            (-1, 1),
            (1, -1),
            (-1, 0),
            (1, 0),
            (0, 1),
            (0, -1),
        ]

        for di, dj in directions:
            ni, nj = di + i, dj + j
            if 0 <= ni < size and 0 <= nj < size:
                neighbors.append((ni, nj))
        return neighbors

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        size = len(grid)
        if grid[0][0] != 0 or grid[size - 1][size - 1] != 0:
            return -1

        if size == 1:
            return 1

        queue = deque([(0, 0)])
        grid[0][0] = 1
        distance = 1

        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                neighbors = self._get_neighbors(i, j, size)

                for ni, nj in neighbors:
                    if ni == size - 1 and nj == size - 1:
                        return distance + 1
                    if grid[ni][nj] == 0:
                        grid[ni][nj] = 1
                        queue.append((ni, nj))
            distance += 1
        return -1


print(Solution().shortestPathBinaryMatrix(grid=[[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
