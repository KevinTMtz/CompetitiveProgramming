#
# LeetCode
#
# Problem - 110
# URL - https://leetcode.com/problems/balanced-binary-tree/description/
#

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right

class Solution:
  def isBalanced(self, root: Optional[TreeNode], first: bool = True) -> bool:
    if not root:
      if first:
        return True

      return 0

    leftH = self.isBalanced(root.left, False)
    rightH = self.isBalanced(root.right, False)

    if leftH is False or rightH is False:
      return False

    if abs(leftH - rightH) > 1:
      return False

    return 1 + max(leftH, rightH)
