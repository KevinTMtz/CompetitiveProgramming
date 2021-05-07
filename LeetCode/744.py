#
# LeetCode
#
# Problem - 744
# URL - https://leetcode.com/problems/find-smallest-letter-greater-than-target/
#

class Solution:
  def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    index = bisect.bisect_right(letters, target)
    return letters[index] if (index != len(letters)) else letters[0]
