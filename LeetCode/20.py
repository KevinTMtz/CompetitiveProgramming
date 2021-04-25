#
# LeetCode
#
# Problem - 20
# URL - https://leetcode.com/problems/valid-parentheses/
#

class Solution:
  def isValid(self, s: str) -> bool:
    queue = []
    for char in s:
      if (char == '(' or char == '[' or char == '{'):
        queue.append(char)
      else:
        if queue:
          poped = queue.pop(-1)

          if ((char == ')' and poped != '(')
              or (char == ']' and poped != '[')
                  or (char == '}' and poped != '{')):
            return False
        else:
          return False

    if queue:
      return False
    else:
      return True
