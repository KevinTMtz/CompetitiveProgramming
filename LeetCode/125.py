#
# LeetCode
#
# Problem - 125
# URL - https://leetcode.com/problems/valid-palindrome/
#

class Solution:
  def isPalindrome(self, s: str) -> bool:
    stack = []

    for letter in s:
      if letter.isalnum():
        stack.append(letter.lower())

    if ''.join(map(str, stack)) == ''.join(map(str, stack[::-1])):
      return True
    return False
