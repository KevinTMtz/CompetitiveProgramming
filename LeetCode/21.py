#
# LeetCode
#
# Problem - 21
# URL - https://leetcode.com/problems/merge-two-sorted-lists/
#

# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next

class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1:
      return list2
    if not list2:
      return list1

    head = None
    if list1.val < list2.val:
      head = list1
      list1 = list1.next
    else:
      head = list2
      list2 = list2.next

    prevNode = head
    while list1 or list2:
      if not list1:
        prevNode.next = list2
        break
      if not list2:
        prevNode.next = list1
        break

      if list1.val < list2.val:
        prevNode.next = list1
        list1 = list1.next
      else:
        prevNode.next = list2
        list2 = list2.next

      prevNode = prevNode.next

    return head
