#
# LeetCode
#
# Problem - 144
# URL - https://leetcode.com/problems/binary-tree-preorder-traversal/description/
#

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right

class Solution:
  def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    preorderList = []

    stack = [root]
    while stack:
      node = stack.pop()

      if not node:
        continue

      preorderList.append(node.val)
      stack.append(node.right)
      stack.append(node.left)

    return preorderList
