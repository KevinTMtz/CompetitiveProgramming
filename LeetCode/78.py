#
# LeetCode
#
# Problem - 78
# URL - https://leetcode.com/problems/subsets/
#

class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    ans = [[]]
    for i in range(0, len(nums)):
      for k in range(0, len(ans)):
        ans.append(ans[k].copy())
      for k in range(len(ans)//2, len(ans)):
        ans[k].append(nums[i])
    return ans
