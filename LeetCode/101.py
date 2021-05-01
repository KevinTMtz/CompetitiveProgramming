#
# LeetCode
#
# Problem - 101
# URL - https://leetcode.com/problems/symmetric-tree/
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def isMirror(self, left: TreeNode, right: TreeNode) -> bool:
    if (left == None and right == None):
      return True
    if (left == None or right == None):
      return False

    return ((left.val == right.val)
            and self.isMirror(left.right, right.left)
            and self.isMirror(left.left, right.right))

  def isSymmetric(self, root: TreeNode) -> bool:
    return self.isMirror(root, root)
