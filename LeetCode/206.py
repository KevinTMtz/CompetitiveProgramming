#
# LeetCode
#
# Problem - 206
# URL - https://leetcode.com/problems/reverse-linked-list/
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
  def reverseList(self, head: ListNode) -> ListNode:
    ansNode = None
    while (head != None):
      ansNode = ListNode(head.val, ansNode)
      head = head.next
    return ansNode
