#
# LeetCode
#
# Problem - 242
# URL - https://leetcode.com/problems/valid-anagram/
#

class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False

    counterS = Counter(s)
    counterT = Counter(t)

    for letter, count in counterS.items():
      if counterS.get(letter) != counterT.get(letter):
        return False

    return True
