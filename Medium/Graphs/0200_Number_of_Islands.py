from typing import List
from collections import deque

"""
LeetCode 200 - Number of Islands

Difficulty: Medium

Time Complexity: O(m * n)
Space Complexity: O(m * n)

Technique:
- Breadth-First Search (BFS)
"""
# class Solution:
#     def get_neighbors(self, i, j, m, n):
#         neighbors = []

#         for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             ni, nj = i + di, j + dj

#             if 0 <= ni < m and 0 <= nj < n:
#                 neighbors.append((ni, nj))

#         return neighbors

#     def numIslands(self, grid: List[List[str]]) -> int:
#         m = len(grid)
#         n = len(grid[0])

#         visited = set()
#         islands = 0

#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == "0" or (i, j) in visited:
#                     continue

#                 visited.add((i, j))
#                 queue = deque([(i, j)])

#                 while queue:
#                     current_i, current_j = queue.popleft()

#                     for neighbor in self.get_neighbors(current_i, current_j, m, n):
#                         ni, nj = neighbor

#                         if grid[ni][nj] == "1" and neighbor not in visited:
#                             visited.add(neighbor)
#                             queue.append(neighbor)

#                 islands += 1

#         return islands


"""
LeetCode 200 - Number of Islands

Difficulty: Medium

Time Complexity: O(m * n)
Space Complexity: O(min(m, n))

Technique:
- Breadth-First Search (BFS)
- In-Place Visited Marking
"""
# from typing import List
# from collections import deque
# class Solution:
#     def get_neighbors(self, i, j, m, n):
#         neighbors = []

#         for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             ni, nj = i + di, j + dj

#             if 0 <= ni < m and 0 <= nj < n:
#                 neighbors.append((ni, nj))

#         return neighbors

#     def numIslands(self, grid: List[List[str]]) -> int:
#         m = len(grid)
#         n = len(grid[0])
#         islands = 0

#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == "0":
#                     continue

#                 islands += 1
#                 grid[i][j] = "0"

#                 queue = deque([(i, j)])

#                 while queue:
#                     current_i, current_j = queue.popleft()

#                     for ni, nj in self.get_neighbors(current_i, current_j, m, n):
#                         if grid[ni][nj] == "1":
#                             grid[ni][nj] = "0"
#                             queue.append((ni, nj))

#         return islands


"""
LeetCode 200 - Number of Islands

Difficulty: Medium

Time Complexity: O(m * n)
Space Complexity: O(m * n)

Technique:
- Depth-First Search (DFS)
- In-Place Visited Marking
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        islands = 0

        def dfs(i, j):
            grid[i][j] = "0"

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj

                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "1":
                    dfs(ni, nj)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1

        return islands


print(
    Solution().numIslands(
        grid=[
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)
