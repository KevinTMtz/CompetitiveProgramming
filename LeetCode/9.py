#
# LeetCode
#
# Problem - 9
# URL - https://leetcode.com/problems/palindrome-number/
#

class Solution:
  def isPalindrome(self, x: int) -> bool:
    if x < 0:
      return False

    tempX = x
    xReversed = 0

    while tempX > 0:
      difference = tempX % 10

      xReversed = xReversed * 10 + difference
      tempX = (tempX - difference) / 10

    return True if xReversed == x else False
