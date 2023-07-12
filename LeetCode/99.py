#
# LeetCode
#
# Problem - 99
# URL - https://leetcode.com/problems/recover-binary-search-tree/description/
#

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right

class Solution:
  def recoverTree(self, root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    badArr = []
    nodesArr = []

    stack = []
    currentNode = root
    while stack or currentNode:
      if currentNode:
        stack.append(currentNode)
        currentNode = currentNode.left
      else:
        currentNode = stack.pop()
        badArr.append(currentNode.val)
        nodesArr.append(currentNode)
        currentNode = currentNode.right

    sortedArr = sorted(badArr)
    for i in range(len(badArr)):
      if badArr[i] != sortedArr[i]:
        nodesArr[i].val = sortedArr[i]
