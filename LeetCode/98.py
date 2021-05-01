#
# LeetCode
#
# Problem - 98
# URL - https://leetcode.com/problems/validate-binary-search-tree/
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def isValidBST(self, root: TreeNode) -> bool:
    if root == None:
      return True

    queue = [(root, float('-inf'), float('inf'))]

    while queue:
      temp, lower, upper = queue.pop(0)

      if temp.val <= lower or temp.val >= upper:
        return False

      if temp.left != None:
        queue.append((temp.left, lower, temp.val))
      if temp.right != None:
        queue.append((temp.right, temp.val, upper))

    return True
