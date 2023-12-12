#
# LeetCode
#
# Problem - 238
# URL - https://leetcode.com/problems/product-of-array-except-self/
#

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    preNums = nums.copy()
    preNums[0] = 1
    suffNums = nums.copy()
    suffNums[len(suffNums) - 1] = 1

    for i in range(1, len(preNums)):
      preNums[i] = preNums[i-1] * nums[i-1]
    print(preNums)

    for i in range(len(suffNums)-2, -1, -1):
      suffNums[i] = suffNums[i+1] * nums[i+1]
    print(suffNums)
    
    return map(lambda preNum,suffNum:preNum*suffNum, preNums, suffNums)