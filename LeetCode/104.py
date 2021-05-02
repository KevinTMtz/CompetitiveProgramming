#
# LeetCode
#
# Problem - 104
# URL - https://leetcode.com/problems/maximum-depth-of-binary-tree/
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def maxDepth(self, root: TreeNode) -> int:
    if root is None:
      return 0

    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
