"""
LeetCode 994 - Rotting Oranges

Difficulty: Medium

Time Complexity: O(m * n)
Space Complexity: O(m * n)

Technique:
- Multi-Source Breadth-First Search (BFS)
"""

from typing import List
from collections import deque


class Solution:
    def _get_neighbors(self, i, j, m, n):
        neighbors = []

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj

            if 0 <= ni < m and 0 <= nj < n:
                neighbors.append((ni, nj))

        return neighbors

    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        m = len(grid)
        n = len(grid[0])
        minutes = -1
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0

        while queue:
            for _ in range(len(queue)):
                current_i, current_j = queue.popleft()
                neighbors = self._get_neighbors(current_i, current_j, m, n)

                for i, j in neighbors:
                    if grid[i][j] == 1:
                        grid[i][j] = 2
                        queue.append((i, j))
                        fresh -= 1

            minutes += 1
        return minutes if fresh == 0 else -1


print(Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
