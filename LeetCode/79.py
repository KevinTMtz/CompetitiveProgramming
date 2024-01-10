#
# LeetCode
#
# Problem - 79
# URL - https://leetcode.com/problems/word-search/
#

class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
    for y in range(len(board)):
      for x in range(len(board[0])):
        if board[y][x] == word[0] and self.existHelper(board, word[1:], dict(), (y,x)):
          return True

    return False

  def existHelper(self, board: List[List[str]], word: str, used_board: dict, coor: (int, int)) -> bool:
    if len(word) <= 0:
      return True

    used_board[coor] = True
    y_coors = [coor[0]-1, coor[0]+1]
    for y_coor in y_coors:
      if (
        y_coor >= 0 and y_coor < len(board)
        and board[y_coor][coor[1]] == word[0]
        and not used_board.get((y_coor, coor[1]), False) 
        and self.existHelper(board, word[1:], used_board, (y_coor, coor[1]))
      ):
        return True

    x_coors = [coor[1]-1, coor[1]+1]
    for x_coor in x_coors:
      if (
        x_coor >= 0 and x_coor < len(board[0])
        and board[coor[0]][x_coor] == word[0]
        and not used_board.get((coor[0], x_coor), False)
        and self.existHelper(board, word[1:], used_board, (coor[0], x_coor))
      ):
        return True

    used_board[coor] = False

