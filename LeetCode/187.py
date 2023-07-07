#
# LeetCode
#
# Problem - 187
# URL - https://leetcode.com/problems/repeated-dna-sequences/description/
#

class Solution:
  def findRepeatedDnaSequences(self, s: str) -> List[str]:
    ans = []
    
    if len(s) < 10:
      return ans

    seriesSet = set()
    for i in range(0, len(s) - 9):
      tempStr = s[i : i + 10]
      if tempStr in seriesSet and not tempStr in ans:
        ans.append(tempStr)
      else:
        seriesSet.add(tempStr)

    return ans
