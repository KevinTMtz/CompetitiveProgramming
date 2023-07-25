#
# LeetCode
#
# Problem - 142
# URL - https://leetcode.com/problems/linked-list-cycle-ii/
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slowNode = head
    fastNode = head
    while fastNode and fastNode.next:
      slowNode = slowNode.next
      fastNode = fastNode.next.next

      if slowNode == fastNode:
        slowNode = head
        while slowNode != fastNode:
          slowNode = slowNode.next
          fastNode = fastNode.next

        return slowNode

    return None
