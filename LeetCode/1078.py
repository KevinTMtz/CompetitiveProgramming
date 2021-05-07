#
# LeetCode
#
# Problem - 1078
# URL - https://leetcode.com/problems/occurrences-after-bigram/
#

class Solution:
  def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
    ans = []
    textArr = text.split()

    for i in range(len(textArr)-2):
      if textArr[i] == first and textArr[i+1] == second:
        ans.append(textArr[i+2])

    return ans
