#
# LeetCode
#
# Problem - 114
# URL - https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
#

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right

class Solution:
  def flatten(self, root: Optional[TreeNode]) -> None:
    preorderList = []

    stack = [root]
    while stack:
      node = stack.pop()

      if not node:
        continue

      preorderList.append(node)
      stack.append(node.right)
      stack.append(node.left)

    for i in range(len(preorderList) - 1):
      preorderList[i].right = preorderList[i + 1]
      preorderList[i].left = None