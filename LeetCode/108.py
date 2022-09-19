#
# LeetCode
#
# Problem - 108
# URL - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/submissions/
#

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right

class Solution:
  def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    if not nums:
      return None
    
    middle = len(nums) // 2
    
    return TreeNode(
      nums[middle], 
      self.sortedArrayToBST(nums[:middle]), 
      self.sortedArrayToBST(nums[middle + 1:])
    )
