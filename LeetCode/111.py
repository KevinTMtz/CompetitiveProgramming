#
# LeetCode
#
# Problem - 111
# URL - https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right

class Solution:
  def minDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0

    minD = float('inf')

    queue = [(root, 1)]
    while queue:
      node, level = queue.pop(0)

      if not node.left and not node.right:
        minD = min(level, minD)

      if node.left:
        queue.append((node.left, level + 1))
      if node.right:
        queue.append((node.right, level + 1))

    return minD
