"""
LeetCode 417 - Pacific Atlantic Water Flow

Difficulty: Medium

Time Complexity: O(m * n)
Space Complexity: O(m * n)

Technique:
- Multi-Source DFS
"""

from typing import List


class Solution:
    def _get_sources(self, c_length, r_length):
        pacific_sources = set()
        atlantic_sources = set()

        for i in range(c_length):
            upper_cell = (0, i)
            lower_cell = (r_length - 1, i)
            pacific_sources.add(upper_cell)
            atlantic_sources.add(lower_cell)

        for i in range(r_length):
            left_cell = (i, 0)
            right_cell = (i, c_length - 1)
            pacific_sources.add(left_cell)
            atlantic_sources.add(right_cell)

        return (pacific_sources, atlantic_sources)

    def _get_neighbors(self, i, j, r_length, c_length):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < r_length and 0 <= nj < c_length:
                yield (ni, nj)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r_length = len(heights)
        c_length = len(heights[0])
        visited_pacific = set()
        visited_atlantic = set()
        pacific_sources, atlantic_sources = self._get_sources(c_length, r_length)

        def dfs(i, j, visited):
            visited.add((i, j))
            for ni, nj in self._get_neighbors(i, j, r_length, c_length):
                if (ni, nj) not in visited and heights[ni][nj] >= heights[i][j]:
                    dfs(ni, nj, visited)

        for i, j in pacific_sources:
            dfs(i, j, visited_pacific)

        for i, j in atlantic_sources:
            dfs(i, j, visited_atlantic)

        return list(visited_atlantic & visited_pacific)
