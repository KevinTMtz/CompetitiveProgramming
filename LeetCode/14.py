#
# LeetCode
#
# Problem - 14
# URL - https://leetcode.com/problems/longest-common-prefix/
#

class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    ans = ''

    index = 0
    tempLetter = ''
    while True:
      for i in range(0, len(strs)):
        if index >= len(strs[i]):
          return ans

        if i == 0:
          tempLetter = strs[i][index]
        elif tempLetter != strs[i][index]:
          return ans

      index += 1
      ans += tempLetter

    return ans
