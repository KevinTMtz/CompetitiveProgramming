#
# LeetCode
#
# Problem - 543
# URL - https://leetcode.com/problems/diameter-of-binary-tree/submissions/
#

class Solution:
  def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    return self.diameterOfBinaryTreeHelper(root)[0]

  def diameterOfBinaryTreeHelper(self, root: Optional[TreeNode]) -> (int, int):
    maxDL, diameterL = 0, 0
    if root.left:
      maxDL, diameterL = self.diameterOfBinaryTreeHelper(root.left)

    maxDR, diameterR = 0, 0
    if root.right:
      maxDR, diameterR = self.diameterOfBinaryTreeHelper(root.right)

    return (
      max(diameterL + diameterR, max(maxDL, maxDR)), 
      max(diameterL + 1, diameterR + 1)
    )