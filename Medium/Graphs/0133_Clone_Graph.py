"""
LeetCode 133 - Clone Graph

Difficulty: Medium

Time Complexity: O(V + E)
Space Complexity: O(V)

Technique:
- Depth-First Search (DFS)
"""

# from typing import Optional


# class Node:
#     def __init__(self, val=0, neighbors=None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []


# class Solution:
#     def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
#         if not node:
#             return

#         clone_dict = {}

#         def _dfs(node):
#             if node in clone_dict:
#                 return clone_dict[node]

#             clone = Node(node.val)
#             clone_dict[node] = clone

#             for neighbor in node.neighbors:
#                 clone.neighbors.append(_dfs(neighbor))

#             return clone

#         return _dfs(node)


"""
LeetCode 133 - Clone Graph

Difficulty: Medium

Time Complexity: O(V + E)
Space Complexity: O(V)

Technique:
- Breadth-First Search (BFS)
"""
# from typing import Optional
# from collections import deque


# class Solution:
#     def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
#         if not node:
#             return None

#         clone_dict = {node: Node(node.val)}
#         queue = deque([node])

#         while queue:
#             current = queue.popleft()

#             for neighbor in current.neighbors:
#                 if neighbor not in clone_dict:
#                     clone_dict[neighbor] = Node(neighbor.val)
#                     queue.append(neighbor)

#                 clone_dict[current].neighbors.append(clone_dict[neighbor])

#         return clone_dict[node]
