#
# LeetCode
#
# Problem - 412
# URL - https://leetcode.com/problems/fizz-buzz/
#

class Solution:
  def fizzBuzz(self, n: int) -> List[str]:
    ansList = []

    for i in range(1, n+1):
      if i % 3 == 0 and i % 5 == 0:
        ansList.append('FizzBuzz')
      elif i % 3 == 0:
        ansList.append('Fizz')
      elif i % 5 == 0:
        ansList.append('Buzz')
      else:
        ansList.append(str(i))

    return ansList
