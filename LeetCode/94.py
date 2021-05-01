#
# LeetCode
#
# Problem - 94
# URL - https://leetcode.com/problems/binary-tree-inorder-traversal/
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def inorderTraversal(self, root: TreeNode) -> List[int]:
    ans = []
    stack = []

    curr = root
    while (curr != None or stack):
      while (curr != None):
        stack.append(curr)
        curr = curr.left

      curr = stack.pop()
      ans.append(curr.val)
      curr = curr.right

    return ans
