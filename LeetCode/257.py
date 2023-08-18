#
# LeetCode
#
# Problem - 257
# URL - https://leetcode.com/problems/binary-tree-paths/
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    if root is None:
      return []

    if root.left is None and root.right is None:
      return [str(root.val)]

    paths = self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)
    for i in range(len(paths)):
      paths[i] = str(root.val) + "->" + paths[i]

    return paths
