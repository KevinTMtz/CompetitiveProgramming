#
# LeetCode
#
# Problem - 297
# URL - https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
#

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
          return '[]'

        queue = [root]
        ansArr = [root.val]
        while queue:
          currentNode = queue.pop(0)

          if currentNode.left:
            queue.append(currentNode.left)

          if currentNode.right:
            queue.append(currentNode.right)

          ansArr.append(currentNode.left.val if currentNode.left else None)
          ansArr.append(currentNode.right.val if currentNode.right else None)

        return str(ansArr)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
          return None

        treeArr = data.strip('[]').split(', ')

        root = TreeNode(treeArr.pop(0), None, None)
        workingArr = [root]
        while treeArr:
          parent = workingArr.pop(0)

          leftVal = treeArr.pop(0)
          if leftVal != 'None':
            leftNode = TreeNode(leftVal, None, None)
            workingArr.append(leftNode)
            parent.left = leftNode

          rightVal = treeArr.pop(0)
          if rightVal != 'None':
            rightNode = TreeNode(rightVal, None, None)
            workingArr.append(rightNode)
            parent.right = rightNode

        return root
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))