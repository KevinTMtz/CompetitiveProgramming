#
# LeetCode
#
# Problem - 2
# URL - https://leetcode.com/problems/add-two-numbers/
#

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
  def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    total = 0

    units = 1
    while (l1 is not None or l2 is not None):
      if (l1 is not None):
        total += units * l1.val
        l1 = l1.next
      if (l2 is not None):
        total += units * l2.val
        l2 = l2.next
      units *= 10

    total = str(total)

    listNodeAns = ListNode(int(total[0]), None)
    for i in range(1, len(total)):
      listNodeAns = ListNode(int(total[i]), listNodeAns)

    return listNodeAns
