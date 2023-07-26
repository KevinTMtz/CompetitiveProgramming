#
# LeetCode
#
# Problem - 96
# URL - https://leetcode.com/problems/unique-binary-search-trees/
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
    arr = []

    node = head
    while node != None:
      arr.append(node.val)
      node = node.next
    node = head

    return self.helper(arr)

  def helper(self, arr: List) -> Optional[TreeNode]:
    if len(arr) <= 0:
      return None

    middle = len(arr) // 2

    return TreeNode(
      arr[middle], 
      self.helper(arr[:middle]), 
      self.helper(arr[middle+1:])
    )
    