#
# LeetCode
#
# Problem - 876
# URL - https://leetcode.com/problems/middle-of-the-linked-list/
#

class Solution:
  def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    node = head

    count = 0
    while node:
      count += 1
      node = node.next

    node = head
    for i in range(int(count/2)):
      node = node.next

    return node
