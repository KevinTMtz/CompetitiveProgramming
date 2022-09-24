#
# LeetCode
#
# Problem - 13
# URL - https://leetcode.com/problems/roman-to-integer/
#

class Solution:
  def romanToInt(self, s: str) -> int:
    ans = 0
    
    romanNums = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000
    }
    
    lastPicked = 0
    for i in range(len(s) - 1, -1, -1):
      currentRomanNum = romanNums[s[i]]
      if currentRomanNum < lastPicked:
        ans -= currentRomanNum
      else:
        ans += currentRomanNum
      
      lastPicked = currentRomanNum
    
    return ans
