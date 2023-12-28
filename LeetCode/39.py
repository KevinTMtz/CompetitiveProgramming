#
# LeetCode
#
# Problem - 39
# URL - https://leetcode.com/problems/combination-sum/
#

class Solution:
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    return self.combinationSumHelper(candidates, target, 1)

  def combinationSumHelper(self, candidates: List[int], target: int, lastNum: int) -> List[List[int]]:
    ans = []

    if target == 0:
      return [ans]

    for candidate in candidates:
      if candidate < lastNum or target - candidate < 0:
        continue

      combinations = self.combinationSumHelper(candidates, target - candidate, candidate)

      for combination in combinations:
        combination.append(candidate)

      ans.extend(combinations)

    return ans
        