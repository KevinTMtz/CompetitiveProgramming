#
# LeetCode
#
# Problem - 112
# URL - https://leetcode.com/problems/path-sum/
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    if not root:
      return False

    currValue = sum-root.val
    if currValue == 0 and root.left == None and root.right == None:
      return True

    return (self.hasPathSum(root.left, currValue) or
            self.hasPathSum(root.right, currValue))
