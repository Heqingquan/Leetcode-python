# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        link = head
        if link.next != None:
            cache = link.next.next
            head = link.next
            head.next = link
            link.next = cache
        else:
            return head
        while True:
            if link.next != None and link.next.next != None:
                cache = link.next
                cache2 = link.next.next.next
                link.next = link.next.next
                link.next.next = cache
                cache.next = cache2
                link = cache
            else:
                return head



