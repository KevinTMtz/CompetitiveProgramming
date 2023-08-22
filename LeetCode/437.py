#
# LeetCode
#
# Problem - 437
# URL - https://leetcode.com/problems/path-sum-iii/
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    return self.pathSumHelper(root, targetSum, [])

  def pathSumHelper(self, root: Optional[TreeNode], targetSum: int, sums: List[int]) -> int:
    if root is None:
      return 0

    count = 0
    newSums = sums.copy()
    for i in range(len(newSums)):
      newSums[i] += root.val

      if newSums[i] == targetSum:
        count += 1

    newSums.append(root.val)
    if root.val == targetSum:
      count += 1

    return (
      count + 
      self.pathSumHelper(root.left, targetSum, newSums) +
      self.pathSumHelper(root.right, targetSum, newSums)
    )
