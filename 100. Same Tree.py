# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p==None) ^ (q==None):
            return False
        if p==None and q == None:
            return True
        queue_p = self.tree2queue(p)
        queue_q = self.tree2queue(q)
        if len(queue_p) != len(queue_q):
            return False
        else:
            for i in range(len(queue_p)):
                if queue_p[i].val != queue_q[i].val:
                    return False
                if (queue_p[i].left == None) ^ (queue_q[i].left == None):
                    return False
                if (queue_p[i].right == None) ^ (queue_q[i].right == None):
                    return False
        return True
    def tree2queue(self,node):
        nodequeue = []
        nodequeue.append(node)
        index = 0
        while index < len(nodequeue):
            if nodequeue[index].left != None:
                nodequeue.append(nodequeue[index].left)
            if nodequeue[index].right != None:
                nodequeue.append(nodequeue[index].right)
            index += 1
        return nodequeue