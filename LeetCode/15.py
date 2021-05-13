#
# LeetCode
#
# Problem - 15
# URL - https://leetcode.com/problems/3sum/
#

class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    resultTriplets = set()

    for i in range(len(nums)-2):
      seenNums = {nums[i+1]}

      for k in range(i+2, len(nums)):
        j = -1*(nums[k]+nums[i])

        if j in seenNums:
          newTriplet = [nums[i], nums[k], j]
          newTriplet.sort()

          resultTriplets.add(tuple(newTriplet))

        seenNums.add(nums[k])

    return resultTriplets
