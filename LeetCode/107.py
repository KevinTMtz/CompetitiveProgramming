#
# LeetCode
#
# Problem - 107
# URL - https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
#

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right

class Solution:
  def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
      return []

    ans = []

    queue = [(root, 0)]
    while queue:
      node, level = queue.pop(0)

      if len(ans) < level + 1:
        ans.insert(0, [])

      ans[len(ans) - 1 - level].append(node.val)

      if node.left:
        queue.append((node.left, level + 1))
      if node.right:
        queue.append((node.right, level + 1))

    return ans
