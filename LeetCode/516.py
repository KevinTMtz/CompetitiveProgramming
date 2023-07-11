#
# LeetCode
#
# Problem - 516
# URL - https://leetcode.com/problems/longest-palindromic-subsequence/
#

class Solution:
  def longestPalindromeSubseq(self, s: str) -> int:
    strLen = len(s)
    if strLen == 1:
      return 1

    dynamicP = {}
    for i in range(0, strLen):
      for j in range(len(s) - 1, -1, -1):
        if s[i] == s[j]:
          dynamicP[(i, j)] = dynamicP.get((i - 1, j + 1), 0) + 1
        else:
          dynamicP[(i, j)] = max(
            dynamicP.get((i - 1, j), 0), 
            dynamicP.get((i, j + 1), 0)
          )

    return dynamicP.get((strLen - 1, 0), 0)
