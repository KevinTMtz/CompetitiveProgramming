#
# LeetCode
#
# Problem - 315
# URL - https://leetcode.com/problems/count-of-smaller-numbers-after-self/
#

class Solution:
  def countSmaller(self, nums: List[int]) -> List[int]:
    numsLength = len(nums)

    ans = [0] * numsLength
    helpingArr = []
    for i in range(numsLength-1, -1, -1):
      index = bisect.bisect_left(helpingArr, nums[i])
      helpingArr.insert(index, nums[i])
      ans[i] = index
    return ans
