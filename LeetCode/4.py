#
# LeetCode
#
# Problem - 4
# URL - https://leetcode.com/problems/median-of-two-sorted-arrays/
#

class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    cont = sorted(nums1 + nums2)
    i = 0
    j = len(cont) - 1
    while i <= j:
      if i == j:
        return cont[i]
      elif i == j - 1:
        return (cont[i] + cont[j])/2
      i += 1
      j -= 1
