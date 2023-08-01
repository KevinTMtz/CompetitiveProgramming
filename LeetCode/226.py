#
# LeetCode
#
# Problem - 226
# URL - https://leetcode.com/problems/invert-binary-tree/
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
      return

    queue = [root]
    while queue:
      currentNode = queue.pop(0)
      currentNode.left, currentNode.right = currentNode.right, currentNode.left

      if not currentNode.left is None:
        queue.append(currentNode.left)
      if not currentNode.right is None: 
        queue.append(currentNode.right)

    return root