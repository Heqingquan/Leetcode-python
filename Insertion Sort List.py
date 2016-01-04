# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        isForward = 1
        forward = None
        SortedHead = head
        head = head.next
        SortedHead.next = None
        while head:
            flag = SortedHead
            while flag.val < head.val and flag.next is not None:
                forward = flag
                flag = flag.next
            if flag.next is None and flag.val < head.val:
                isForward = 0
            cache = head.next
            if isForward == 0:
                head.next = flag.next
                flag.next = head
                isForward = 1
            else:
                head.next = flag
                if flag == SortedHead:
                    SortedHead = head
                else:
                    forward.next = head
            head = cache
        return SortedHead


