#
# LeetCode
#
# Problem - 46
# URL - https://leetcode.com/problems/permutations/
#

class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
    if len(nums) == 1:
      return [nums]
    
    ans = []
    
    for i in range(len(nums)):
      permutations = self.permute(nums[:i] + nums[i+1:])
      
      for permutation in permutations:
        permutation.append(nums[i])

        ans.append(permutation)

    return ans
