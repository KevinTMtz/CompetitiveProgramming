#
# LeetCode
#
# Problem - 429
# URL - https://leetcode.com/problems/n-ary-tree-level-order-traversal/submissions/
#

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
  def levelOrder(self, root: 'Node') -> List[List[int]]:
    if root is None:
      return []

    ans = []
    
    queue = [(root, 0)]
    while queue:
      node, level = queue.pop(0)

      if len(ans) < level + 1:
        ans.append([])

      ans[level].append(node.val)

      for child in node.children:
        queue.append((child, level + 1))

    return ans