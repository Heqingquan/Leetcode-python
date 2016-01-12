# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        nodeQueue = []
        flag = 0
        loc = 0
        resultList = []
        nodeQueue.append(root)
        resultList.append([])
        resultList[0].append(root.val)
        print(resultList[0])
        while loc < len(nodeQueue):
            if nodeQueue[loc].left != None:
                nodeQueue.append(nodeQueue[loc].left)
            if nodeQueue[loc].right != None:
                nodeQueue.append(nodeQueue[loc].right)
            if flag == loc and len(nodeQueue)-1 != loc:
                resultList.append([])
                for i in range(flag+1,len(nodeQueue)):
                    # print(nodeQueue[i].val)
                    resultList[-1].append(nodeQueue[i].val)
                flag = len(nodeQueue)-1
            loc += 1
        resultList.reverse()
        return resultList