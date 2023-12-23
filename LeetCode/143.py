#
# LeetCode
#
# Problem - 143
# URL - https://leetcode.com/problems/reorder-list/description/
#

# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next

class Solution:
  def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    stack = []
    temp = head
    while temp:
      stack.append(temp)
      temp = temp.next

    temp = head
    for _ in range(len(stack) // 2):
      to_insert = stack.pop()
      stack[-1].next = None

      temp.next, to_insert.next, temp = to_insert, temp.next, temp.next
    
    return head
