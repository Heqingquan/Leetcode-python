# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        link = head
        while link.next is not None:
            if link.value == link.next.value:
                link.next = link.next.next
            else:
                link = link.next

