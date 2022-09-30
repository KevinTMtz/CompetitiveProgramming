#
# LeetCode
#
# Problem - 145
# URL - https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    preorderList = []

    stack = [root]
    while stack:
      node = stack.pop()

      if not node:
        continue

      preorderList.append(node.val)
      stack.append(node.left)
      stack.append(node.right)

    return preorderList[::-1]
