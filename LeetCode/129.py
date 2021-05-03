#
# LeetCode
#
# Problem - 129
# URL - https://leetcode.com/problems/sum-root-to-leaf-numbers/
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def sumNumbers(self, root: TreeNode) -> int:
    return self.sumNumbersHelper(root, 0)

  def sumNumbersHelper(self, root: TreeNode, count: int) -> int:
    if not root:
      return count

    if root.left == None and root.right == None:
      return count*10 + root.val
    elif root.left == None:
      return self.sumNumbersHelper(root.right, count*10+root.val)
    elif root.right == None:
      return self.sumNumbersHelper(root.left, count*10+root.val)

    return (self.sumNumbersHelper(root.left, count*10+root.val) +
            self.sumNumbersHelper(root.right, count*10+root.val))
