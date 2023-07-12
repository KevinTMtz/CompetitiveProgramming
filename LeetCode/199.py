#
# LeetCode
#
# Problem - 199
# URL - https://leetcode.com/problems/binary-tree-right-side-view/description/
#

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right

class Solution:
  def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    if root is None:
      return []

    ans = []
    stack = [(root, 0)]
    while stack:
      (node, level) = stack.pop()

      if len(ans) == level:
        ans.append(node.val)
      
      if node.left:
        stack.append((node.left, level + 1))
      if node.right:
        stack.append((node.right, level + 1))

    return ans