# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.depth = 9999999
        self.findDepth(root,1)
        return self.depth
    def findDepth(self,node,depth):
        if node.left == None and node.right == None:
            if depth < self.depth:
                self.depth = depth
            return
        depth += 1
        if node.left != None:
            self.findDepth(node.left,depth)
        if node.right != None:
            self.findDepth(node.right,depth)