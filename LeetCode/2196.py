#
# LeetCode
#
# Problem - 2196
# URL - https://leetcode.com/problems/create-binary-tree-from-descriptions/description/
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
    nodesMap = dict()
    noParentsMap = dict()
    for description in descriptions:
      parent, child, isLeft = description

      parentNode = None
      if parent in nodesMap:
        parentNode = nodesMap[parent]
      else:
        parentNode = TreeNode(parent, None, None)
        nodesMap[parent] = parentNode
        noParentsMap[parent] = parentNode

      childNode = None
      if child in nodesMap:
        childNode = nodesMap[child]
      else:
        childNode = TreeNode(child, None, None)
        nodesMap[child] = childNode

      if child in noParentsMap:
        noParentsMap.pop(child)

      if isLeft:
        parentNode.left = childNode
      else:
        parentNode.right = childNode

    return list(noParentsMap.values())[0]
