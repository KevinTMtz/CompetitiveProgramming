#
# LeetCode
#
# Problem - 74
# URL - https://leetcode.com/problems/search-a-2d-matrix/
#

class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    matrixRowsN = len(matrix)
    matrixColumnsN = len(matrix[0])

    topRow = 0
    bottomRow = matrixRowsN - 1
    while topRow <= bottomRow:
      middleRow = (topRow + bottomRow) // 2

      doRowSearch = False
      if matrix[middleRow][0] <= target:
        if matrix[middleRow][-1] >= target:
          doRowSearch = True
        else:
          topRow = middleRow + 1
      else:
        bottomRow = middleRow - 1

      if doRowSearch:        
        l = 0
        r = matrixColumnsN - 1
        while l <= r:
          middle = (l + r) // 2

          if matrix[middleRow][middle] == target:
            return True
          elif matrix[middleRow][middle] > target:
            r = middle - 1
          else:
            l = middle + 1

        return False

    return False
