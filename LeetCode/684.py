#
# LeetCode
#
# Problem - 684
# URL - https://leetcode.com/problems/redundant-connection/
#

class Solution:
  def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    parents = dict()
    ranks = dict()

    for edge in edges:
      if not edge[0] in parents:
        parents[edge[0]] = edge[0]
        ranks[edge[0]] = 1
      if not edge[1] in parents:
        parents[edge[1]] = edge[1]
        ranks[edge[1]] = 1

      parent_1 = self.find_parent(edge[0], parents)
      parent_2 = self.find_parent(edge[1], parents)
      if parent_1 == parent_2:
        return edge

      if ranks[parent_1] > ranks[parent_2]:
        ranks[parent_1] += ranks[parent_2]
        parents[parent_2] = self.find_parent(parent_1, parents)
      else:
        ranks[parent_2] += ranks[parent_1]
        parents[parent_1] = self.find_parent(parent_2, parents)

  def find_parent(self, n: int, parents: dict()) -> int:
    parent = parents[n]
    while parent != parents[parent]:
      parents[parent] = parents[parents[parent]]
      parent = parents[parent]

    return parent
