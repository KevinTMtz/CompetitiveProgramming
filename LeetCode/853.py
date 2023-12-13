#
# LeetCode
#
# Problem - 853
# URL - https://leetcode.com/problems/car-fleet/solutions/
#

class Solution:
  def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    pairs = sorted(map(lambda p,s:[p,s], position, speed))

    fleets = 1
    for i in range(len(position) - 2, -1, -1):
      maxDriven1 = (target - pairs[i][0]) / pairs[i][1]
      maxDriven2 = (target - pairs[i + 1][0]) / pairs[i + 1][1]

      if maxDriven1 > maxDriven2:
        fleets += 1
      else:
        pairs[i] = pairs[i + 1]

    return fleets
