#
# LeetCode
#
# Problem - 350
# URL - https://leetcode.com/problems/intersection-of-two-arrays-ii/
#

class Solution:
  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    seen = {}
    ans = []
    for num in nums1:
      seen[num] = seen.get(num, 0) + 1

    for num in nums2:
      if num in seen:
        ans.append(num)
        seen[num] -= 1
        if seen[num] == 0:
          del seen[num]

    return ans
