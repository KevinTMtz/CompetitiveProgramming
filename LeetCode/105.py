#
# LeetCode
#
# Problem - 105
# URL - https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    if not inorder:
      return None

    r = preorder.pop(0)
    root = TreeNode(r)
    index = inorder.index(r)

    root.right = self.buildTree(preorder[index:], inorder[index+1:])
    root.left = self.buildTree(preorder, inorder[:index])

    return root
