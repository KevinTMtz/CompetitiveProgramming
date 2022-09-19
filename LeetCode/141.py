#
# LeetCode
#
# Problem - 141
# URL - https://leetcode.com/problems/linked-list-cycle/
#

# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, x):
#     self.val = x
#     self.next = None

class Solution:
  def hasCycle(self, head: Optional[ListNode]) -> bool:
    nodesSet = set()

    tempNode = head
    while tempNode:
      if tempNode in nodesSet:
        return True
      else:
        nodesSet.add(tempNode)
        
      tempNode = tempNode.next

    return False
        