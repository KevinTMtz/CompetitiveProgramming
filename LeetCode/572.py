#
# LeetCode
#
# Problem - 572
# URL - https://leetcode.com/problems/subtree-of-another-tree/
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    queue = [root]

    while queue:
      currentNode = queue.pop(0)

      if (
        currentNode.val == subRoot.val and 
        self.sameTreesCheck(currentNode, subRoot)
      ):
        return True
      
      if currentNode.left:
        queue.append(currentNode.left)

      if currentNode.right:
        queue.append(currentNode.right)

    return False

  def sameTreesCheck(self, tree1: TreeNode, tree2: TreeNode) -> bool:
    queue = [(tree1, tree2)]
    while queue:
      node1, node2 = queue.pop(0)

      if node1 is None:
        if node2 is None:
          continue
        else:
          return False
      if node2 is None:
        return False


      if node1.val != node2.val:
        return False
      else:
        queue.append((node1.left, node2.left))
        queue.append((node1.right, node2.right))

    return True