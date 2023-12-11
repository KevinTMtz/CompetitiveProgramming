#
# LeetCode
#
# Problem - 49
# URL - https://leetcode.com/problems/group-anagrams/
#

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams = dict()

    for word in strs:
      key = ''.join(sorted(word))

      if key in anagrams:
        anagrams[key].append(word)
      else:
        anagrams[key] = [word]

    return list(anagrams.values())
