#
# LeetCode
#
# Problem - 189
# URL - https://leetcode.com/problems/rotate-array/
#

class Solution:
  def rotate(self, nums: List[int], k: int) -> None:
    numsLen = len(nums)

    if numsLen == 1:
      return

    k = k % numsLen

    self.reverseNums(nums, 0, numsLen)
    self.reverseNums(nums, 0, k)
    self.reverseNums(nums, k, numsLen)

  def reverseNums(self, nums, index1, index2):
    index2 -= 1

    while index1 < index2:
      nums[index1], nums[index2] = nums[index2], nums[index1]

      index1 += 1
      index2 -= 1
