#
# LeetCode
#
# Problem - 113
# URL - https://leetcode.com/problems/path-sum-ii/
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    if root is None:
      return []

    newTargetSum = targetSum - root.val

    if root.left is None and root.right is None:
      if newTargetSum == 0:
        return [[root.val]]
      else:
        return []

    leftArr = self.pathSum(root.left, newTargetSum)
    rightArr = self.pathSum(root.right, newTargetSum)
    
    resultArr = [*leftArr, *rightArr]
    for i in range(len(resultArr)):
      resultArr[i] = [root.val, *resultArr[i]]

    return resultArr
