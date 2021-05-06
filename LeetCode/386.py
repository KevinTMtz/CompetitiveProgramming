#
# LeetCode
#
# Problem - 386
# URL - https://leetcode.com/problems/lexicographical-numbers/
#

class Solution:
  def lexicalOrder(self, n: int) -> List[int]:
    ans = []

    for i in range(1, n+1):
      ans.insert(bisect.bisect_left(ans, str(i)), str(i))

    return ans
