#
# LeetCode
#
# Problem - 1143
# URL - https://leetcode.com/problems/longest-common-subsequence/description/
#

class Solution:
  def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    dynamicP = {}

    for i in range(len(text1)):
      for j in range(len(text2)):
        if text1[i] == text2[j]:
          dynamicP[(i, j)] = dynamicP.get((i-1, j-1), 0) + 1
        else:
          dynamicP[(i, j)] = max(
            dynamicP.get((i-1, j), 0), 
            dynamicP.get((i, j-1), 0)
          )

    return dynamicP[(len(text1) - 1, len(text2) - 1)]
