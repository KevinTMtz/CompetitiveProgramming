#
# LeetCode
#
# Problem - 383
# URL - https://leetcode.com/problems/ransom-note/
#

class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    while ransomNote:
      ransomNoteChar = ransomNote[0]
      indexInMagazine = magazine.find(ransomNoteChar)

      if indexInMagazine != -1:
        magazine = magazine[:indexInMagazine] + magazine[indexInMagazine+1:]
        ransomNote = ransomNote[1:]
      else:
        return False

    return True
