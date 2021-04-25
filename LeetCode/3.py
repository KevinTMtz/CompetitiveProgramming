#
# LeetCode
#
# Problem - 3
# URL - https://leetcode.com/problems/longest-substring-without-repeating-characters/
#

class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    maxCount = 0
    for i in range(0, len(s)):  # O(n)
      setFeik = {s[i]}
      count = 1
      for k in range(i+1, len(s)):  # O(n)
        if (not s[k] in setFeik):  # O(1)
          setFeik.add(s[k])
          count += 1
        else:
          break

      maxCount = max(maxCount, count)

    return maxCount
