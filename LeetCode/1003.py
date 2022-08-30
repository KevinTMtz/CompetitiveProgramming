#
# LeetCode
#
# Problem - 1003
# URL - https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/
#

class Solution:
  def isValid(self, s: str) -> bool:
    while s:
      position = s.find('abc')

      if position != -1:
        s = s[: position] + s[position + 3:]
      else:
        return False

    return True
