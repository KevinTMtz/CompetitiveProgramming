#
# LeetCode
#
# Problem - 344
# URL - https://leetcode.com/problems/reverse-string/
#

class Solution:
  def reverseString(self, s: List[str]) -> None:
    for i in range(floor(len(s) / 2)):
      s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
