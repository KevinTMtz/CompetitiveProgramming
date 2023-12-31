#
# LeetCode
#
# Problem - 133
# URL - https://leetcode.com/problems/clone-graph/
#

"""
# Definition for a Node.
class Node:
  def __init__(self, val = 0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
  def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    if node is None:
      return node

    old_to_new = dict()
    old_to_new[node] = Node(node.val, [])

    nodes_queue = [node]
    while nodes_queue:
      old_node = nodes_queue.pop(0)

      for neighbor in old_node.neighbors:
        if not neighbor in old_to_new:
          old_to_new[neighbor] = Node(neighbor.val, [])
          nodes_queue.append(neighbor)

        old_to_new[old_node].neighbors.append(old_to_new[neighbor])
      
    return old_to_new[node]
