#
# LeetCode
#
# Problem - 347
# URL - https://leetcode.com/problems/top-k-frequent-elements/
#

class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = dict()

    for num in nums:
      if num in count:
        count[num] += 1
      else:
        count[num] = 1

    return [
      i[0] for i in sorted(
        count.items(), 
        key=lambda x: x[1], 
        reverse=True
      )
    ][:k]
