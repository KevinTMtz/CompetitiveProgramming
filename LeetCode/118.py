#
# LeetCode
#
# Problem - 118
# URL - https://leetcode.com/problems/pascals-triangle/
#

class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    pascalTriangle = []
    
    for level in range(numRows):
      pascalTriangle.append([])
      
      for i in range(level + 1):
        if i == 0 or i == level:
          pascalTriangle[level].append(1)
        else:
          pascalTriangle[level].append(
            pascalTriangle[level - 1][i - 1] + pascalTriangle[level - 1][i] 
          )
    
    return pascalTriangle
