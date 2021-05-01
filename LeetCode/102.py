#
# LeetCode
#
# Problem - 102
# URL - https://leetcode.com/problems/binary-tree-level-order-traversal/
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def levelOrder(self, root: TreeNode) -> List[List[int]]:
    ans = []

    if not root:
      return ans

    queue = [(root, 0)]
    while queue:
      root, depth = queue.pop(0)

      if (len(ans) < depth+1):
        ans.append([])

      ans[depth].append(root.val)

      if (not root.left is None):
        queue.append((root.left, depth + 1))

      if (not root.right is None):
        queue.append((root.right, depth + 1))

    return ans
