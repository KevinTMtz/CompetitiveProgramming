#
# LeetCode
#
# Problem - 19
# URL - https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#

# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next

class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if not head.next:
      return None

    count = 0

    nodesDict = dict()
    tempNode = head
    while tempNode:
      count += 1
      nodesDict[count] = tempNode
      tempNode = tempNode.next

    if count == n:
      return head.next
    else:
      nodesDict.get(count - n).next = nodesDict.get(count - n + 2)
      return head
