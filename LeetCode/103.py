#
# LeetCode
#
# Problem - 103
# URL - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
#

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right

class Solution:
  def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
      return []

    ans = []
    queue = [(root, 0)]
    while queue:
      (node, level) = queue.pop()

      levelCheck = level % 2 == 0

      if level == len(ans):
        ans.append([node.val])
      else:
        if levelCheck:
          ans[level].insert(0, node.val)
        else:
          ans[level].append(node.val)

      if levelCheck:
        if node.left:
          queue.append((node.left, level + 1))
        if node.right:
          queue.append((node.right, level + 1))
      else:
        if node.right:
          queue.insert(0, (node.right, level + 1))
        if node.left:
          queue.insert(0, (node.left, level + 1))

    return ans
