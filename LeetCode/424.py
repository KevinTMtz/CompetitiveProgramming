#
# LeetCode
#
# Problem - 424
# URL - https://leetcode.com/problems/longest-repeating-character-replacement/
#

class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    count = dict()
    max_count = 0

    l = 0
    for r in range(len(s)):
      count[s[r]] = 1 + count.get(s[r], 0)

      while (r - l + 1) - max(count.values()) > k:
        count[s[l]] -= 1
        l += 1

      max_count = max(max_count, r - l + 1)

    return max_count
