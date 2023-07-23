#
# LeetCode
#
# Problem - 2461
# URL - https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/
#

class Solution:
  def maximumSubarraySum(self, nums: List[int], k: int) -> int:
    maxSum = 0

    validNums = 0
    numsCount = {}
    currentSum = 0
    for i in range(len(nums)):
      if i >= k:
        firstNum = nums[i - k]
        currentSum -= firstNum
        numsCount[firstNum] -= 1

        if numsCount.get(firstNum) == 0:
          validNums -= 1

      currentSum += nums[i]
      numsCount[nums[i]] = numsCount.get(nums[i], 0) + 1

      if numsCount[nums[i]] == 1:
        validNums += 1

      if validNums == k:
        maxSum = max(maxSum, currentSum)

    return maxSum