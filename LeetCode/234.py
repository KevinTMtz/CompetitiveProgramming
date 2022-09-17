#
# LeetCode
#
# Problem - 234
# URL - https://leetcode.com/problems/palindrome-linked-list/
#

# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next

class Solution:
  def isPalindrome(self, head: Optional[ListNode]) -> bool:
    nodesStack = []

    tempNode = head
    while tempNode:
      nodesStack.append(tempNode.val)
      tempNode = tempNode.next

    tempNode = head
    while tempNode:
      val = nodesStack.pop()
      if val != tempNode.val:
        return False

      tempNode = tempNode.next

    return True
