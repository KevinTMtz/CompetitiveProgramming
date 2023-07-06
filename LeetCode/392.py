#
# LeetCode
#
# Problem - 392
# URL - https://leetcode.com/problems/is-subsequence/
#

class Solution:
  def isSubsequence(self, s: str, t: str) -> bool:
    index = 0

    for letter in t:
      if index == len(s):
        return True

      if letter == s[index]:
        index += 1

    return index == len(s)
