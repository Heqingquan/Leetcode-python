'''
解题思路：
1,将树以广度优先展开。（queue）
2、记录每行最后一个的位置，即为右视图
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        queue = []
        rightSeeNode = []
        queue.append(root)
        rightSeeNode.append(0)
        flag = 0
        while flag != len(queue):
            if queue[flag].left:
                queue.append(queue[flag].left)
            if queue[flag].right:
                queue.append(queue[flag].right)
            if flag == rightSeeNode[len(rightSeeNode)-1] and flag != len(queue)-1:
                rightSeeNode.append(len(queue)-1)
            flag += 1
        SeeView = [0]*len(rightSeeNode)
        for i in range(len(rightSeeNode)):
            SeeView[i] = queue[rightSeeNode[i]].val
        return SeeView
        


