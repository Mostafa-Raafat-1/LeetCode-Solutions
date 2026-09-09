"""
LeetCode 695 - Max Area of Island

Difficulty: Medium

Time Complexity: O(m * n)
Space Complexity: O(m * n)

Technique:
- Depth-First Search (DFS)
- In-Place Visited Marking
"""

# from typing import List


# class Solution:
#     def _get_neighbors(self, i, j, m, n):
#         directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#         for di, dj in directions:
#             ni, nj = i + di, j + dj

#             if 0 <= ni < m and 0 <= nj < n:
#                 yield ni, nj

#     def _area(self, i, j, m, n, grid):
#         area = 1

#         for ni, nj in self._get_neighbors(i, j, m, n):
#             if grid[ni][nj] == 1:
#                 grid[ni][nj] = 0
#                 area += self._area(ni, nj, m, n, grid)

#         return area

#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         m = len(grid)
#         n = len(grid[0])
#         max_area = 0

#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 0:
#                     continue

#                 grid[i][j] = 0
#                 max_area = max(max_area, self._area(i, j, m, n, grid))

#         return max_area


"""
LeetCode 695 - Max Area of Island

Difficulty: Medium

Time Complexity: O(m * n)
Space Complexity: O(min(m, n))

Technique:
- Breadth-First Search (BFS)
- In-Place Visited Marking
"""

from typing import List
from collections import deque


class Solution:
    def _get_neighbors(self, i, j, m, n):
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for di, dj in directions:
            ni, nj = i + di, j + dj

            if 0 <= ni < m and 0 <= nj < n:
                neighbors.append((ni, nj))

        return neighbors

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        max_area = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                grid[i][j] = 0
                queue.append((i, j))
                current = 1

                while queue:
                    current_i, current_j = queue.popleft()
                    neighbors = self._get_neighbors(current_i, current_j, m, n)

                    for ni, nj in neighbors:
                        if grid[ni][nj] == 1:
                            current += 1
                            grid[ni][nj] = 0
                            queue.append((ni, nj))

                    max_area = max(max_area, current)

        return max_area


print(
    Solution().maxAreaOfIsland(
        grid=[
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]
    )
)
