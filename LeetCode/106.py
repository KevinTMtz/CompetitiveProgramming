#
# LeetCode
#
# Problem - 106
# URL - https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    if not inorder:
      return None

    r = postorder.pop()
    root = TreeNode(r)
    index = inorder.index(r)

    root.right = self.buildTree(inorder[index+1:], postorder)
    root.left = self.buildTree(inorder[:index], postorder)

    return root
