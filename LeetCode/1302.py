#
# LeetCode
#
# Problem - 1302
# URL - https://leetcode.com/problems/deepest-leaves-sum/
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def deepestLeavesSum(self, root: TreeNode) -> int:
    if root is None:
      return 0

    queue = [(root, 0)]
    maxDept = 0
    ans = 0

    while (queue):
      temp, dept = queue.pop(0)
      if dept == maxDept:
        ans += temp.val
      elif dept > maxDept:
        maxDept = dept
        ans = temp.val

      if temp.left != None:
        queue.append((temp.left, dept+1))

      if temp.right != None:
        queue.append((temp.right, dept+1))

    return ans
