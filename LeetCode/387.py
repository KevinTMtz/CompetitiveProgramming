#
# LeetCode
#
# Problem - 387
# URL - https://leetcode.com/problems/first-unique-character-in-a-string/
#

class Solution:
  def firstUniqChar(self, s: str) -> int:
    for letter, count in OrderedDict(Counter(s)).items():
      if count == 1:
        return s.index(letter)

    return -1
