#
# LeetCode
#
# Problem - 230
# URL - https://leetcode.com/problems/kth-smallest-element-in-a-bst/
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    helper, ans = self.kthSmallestHelper(root, k)

    return ans

  def kthSmallestHelper(self, root: Optional[TreeNode], k: int) -> (int, int):
    if root is None:
      return 0, 0

    totalL, ans = self.kthSmallestHelper(root.left, k)
    if ans > 0:
      return 0, ans

    total = totalL + 1
    if total == k:
      return total, root.val

    totalR, ans = self.kthSmallestHelper(root.right, k - total)
    if ans > 0:
      return 0, ans

    return total + totalR, 0
