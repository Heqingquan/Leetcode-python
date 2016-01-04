# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        l = []
        self.aList(l,root)
        for i in range(len(l)-1):
            l[i].right = l[i+1]
            l[i].left = None
        l[len(l)-1].right = None

    def aList(self,l,root):
        l.append(root)
        if root.left != None:
            aList(root.left)
        if root.right != None:
            aList(root.right)
