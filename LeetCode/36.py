#
# LeetCode
#
# Problem - 36
# URL - https://leetcode.com/problems/valid-sudoku/submissions/
#

class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    columnSet = [set() for i in range(9)]
    for rowI in range(9):
      rowSet = set()

      for columnI in range(9):
        if rowI % 3 == 0 and columnI % 3 == 0:
          subBoxSet = set()

          for i in range(3):
            for j in range(3):
              subBoxNum = board[rowI + i][columnI + j]

              if subBoxNum == '.':
                continue

              if subBoxNum in subBoxSet:
                return False

              subBoxSet.add(subBoxNum)

        num = board[rowI][columnI]

        if num == '.':
          continue

        if num in rowSet:
          return False

        if num in columnSet[columnI]:
          return False

        rowSet.add(num)
        columnSet[columnI].add(num)

    return True
