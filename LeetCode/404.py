#
# LeetCode
#
# Problem - 404
# URL - https://leetcode.com/problems/sum-of-left-leaves/
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def sumOfLeftLeaves(self, root: TreeNode) -> int:
    if root is None:
      return 0

    stack = [root]

    ans = 0

    while (stack):
      temp = stack.pop(0)

      if not temp.left is None:
        stack.append(temp.left)

        if temp.left.right is None and temp.left.left is None:
          ans += temp.left.val

      if not temp.right is None:
        stack.append(temp.right)

    return ans
