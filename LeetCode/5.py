#
# LeetCode
#
# Problem - 5
# URL - https://leetcode.com/problems/longest-palindromic-substring/
#

class Solution:
  def longestPalindrome(self, s: str) -> str:
    maxSize = 0
    longestPalindrome = ''

    for i in range(len(s)):
      l = i
      r = i

      while l > 0 and s[l - 1] == s[l]:
        l -= 1

      while r < len(s) - 1 and s[r] == s[r + 1]:
        r += 1

      while l > 0 and r < len(s) - 1 and s[l - 1] == s[r + 1]:
        l -= 1
        r += 1

      if r - l + 1 > maxSize:
        maxSize = r - l + 1
        longestPalindrome = s[l:r + 1]

        if maxSize == len(s):
          break

    return longestPalindrome
