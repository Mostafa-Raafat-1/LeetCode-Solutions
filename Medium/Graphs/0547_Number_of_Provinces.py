"""
LeetCode 547 - Number of Provinces

Difficulty: Medium

Time Complexity: O(n²)
Space Complexity: O(n)

Technique:
- Breadth-First Search (BFS)
"""

# from typing import List
# from collections import deque


# class Solution:
#     def _retrieve_neighbors(self, isConnected, index):
#         neighbors = []

#         for i, val in enumerate(isConnected[index]):
#             if val == 1 and i != index:
#                 neighbors.append(i)

#         return neighbors

#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         provinces = 0
#         visited = set()
#         queue = deque()

#         for city in range(len(isConnected)):
#             if city in visited:
#                 continue

#             queue.append(city)
#             visited.add(city)

#             while queue:
#                 index = queue.popleft()
#                 neighbors = self._retrieve_neighbors(isConnected, index)

#                 for neighbor in neighbors:
#                     if neighbor not in visited:
#                         queue.append(neighbor)
#                         visited.add(neighbor)

#             provinces += 1

#         return provinces


"""
LeetCode 547 - Number of Provinces

Difficulty: Medium

Time Complexity: O(n²)
Space Complexity: O(n)

Technique:
- Depth-First Search (DFS)
"""
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = set()
        n = len(isConnected)

        def dfs(i):
            visited.add(i)
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1 and j not in visited:
                    dfs(j)

        for i in range(n):
            if i not in visited:
                provinces += 1
                dfs(i)

        return provinces


print(Solution().findCircleNum(isConnected=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
