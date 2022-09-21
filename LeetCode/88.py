#
# LeetCode
#
# Problem - 88
# URL - https://leetcode.com/problems/merge-sorted-array/
#

class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    lastIndex = None
    while nums2:
      numToAdd = nums2.pop(0)
      
      for i in range(lastIndex if lastIndex else 0, len(nums1)):
        if len(nums1) - len(nums2) <= i + 1 or nums1[i] >= numToAdd:
          tempNum = numToAdd
          for j in range(i, len(nums1)):
            nums1[j], tempNum = tempNum, nums1[j]
          
          lastIndex = i+1
          break
