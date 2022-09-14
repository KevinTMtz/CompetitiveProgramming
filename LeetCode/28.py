#
# LeetCode
#
# Problem - 28
# URL - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
#

class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    if len(haystack) < len(needle):
      return -1
    elif needle == "":
      return 0

    nextSearch = 0
    for i in range(0, len(haystack) - len(needle) + 1):
      if haystack[i:i + len(needle)] == needle:
        return i

    return -1
