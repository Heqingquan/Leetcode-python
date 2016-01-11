'''
手残实现了一个堆排序，然并卵
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        k = 0
        while True:
            if lists[k] == None:
                del lists[k]
            else:
                k += 1
            if k == len(lists):
                break
        if len(lists) == 0:
            return None
        self.manageHeap(lists)
        head = lists[0]
        link = head
        while True:
            lists[0] = lists[0].next
            if lists[0] == None:
                lists[0] = lists[-1]
                lists.pop()
            if len(lists) == 0:
                break
            self.downTree(lists,0)
            link.next = lists[0]
            link = link.next
        return head



    def downTree(self,lists,n):
        if self.hasRight(lists,n) and lists[n].val > lists[self.getright(n)].val:
            lists[n],lists[self.getright(n)] = lists[self.getright(n)],lists[n]
            self.downTree(lists,self.getright(n))
        if self.hasLeft(lists,n) and lists[n].val > lists[self.getleft(n)].val:
            lists[n],lists[self.getleft(n)] = lists[self.getleft(n)],lists[n]
            self.downTree(lists,self.getleft(n))
        return


    def manageHeap(self,lists):
        for i in range(len(lists)/2-1,-1,-1):
            self.rotateTree(lists,i)
            # self.showList(lists)


    def rotateTree(self,lists,n):
        # print(n)
        if self.hasRight(lists,n) and lists[n].val > lists[self.getright(n)].val:
            lists[n],lists[self.getright(n)] = lists[self.getright(n)],lists[n]
        if self.hasLeft(lists,n) and lists[n].val > lists[self.getleft(n)].val:
            # cache = lists[n]
            # lists[n] = lists[self.getleft(n)]
            # lists[self.getleft(n)] = cache
            lists[n],lists[self.getleft(n)] = lists[self.getleft(n)],lists[n]
            
    def showList(self,lists):
        for i in lists:
            print i.val,
        print ('')


    def hasLeft(self,lists,num):
        return self.getleft(num) < len(lists)
    def hasRight(self,lists,num):
        return self.getright(num) < len(lists)
    def getleft(self,num):
        return 2*num+1
    def getright(self,num):
        return 2*num+2
        '''
    def findTotalNum(self,lists,l):
        for i in lists:
            head = i
            while head:
                l.append(head)
                # print (head.val)
                head = head.next
        '''
