#
# LeetCode
#
# Problem - 100
# URL - https://leetcode.com/problems/same-tree/
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def isSameTree(self, left: TreeNode, right: TreeNode) -> bool:
    queue = [(left, right)]

    while queue:
      p, q = queue.pop(0)

      if p != None and q != None:
        if p.val != q.val:
          return False

        queue.append((p.left, q.left))
        queue.append((p.right, q.right))
      else:
        if p != q:
          return False

    return True
