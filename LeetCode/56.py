#
# LeetCode
#
# Problem - 56
# URL - https://leetcode.com/problems/merge-intervals/
#

class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    
    index = 0
    ans = []
    while index < len(intervals):
      next_index = index
      for i in range(index + 1, len(intervals)):
        if intervals[index][1] >= intervals[i][0]:
          intervals[index][1] = max(intervals[index][1], intervals[i][1])
        else:
          break

        next_index += 1

      ans.append(intervals[index])
      index = next_index + 1

    return ans
