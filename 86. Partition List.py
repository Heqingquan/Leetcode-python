# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        #get the flag of the list
        if head == None:
            return None
        flag = head
        link = head
        while flag != None:
            if flag.val >= x:
                break
            link = flag
            flag = flag.next
        # print("partition_end_1")

        if flag == None:
            return head
        cache = flag
        cache_link = flag
        while cache !=None:
            if cache.val < x:
                data = self.Cut_link(cache_link)
                if flag == head:
                    data.next = head
                    head = data
                    flag == None
                    link = head
                else:
                    data.next = link.next
                    link.next = data
                    link = data
            cache_link = cache
            cache = cache.next
        # print("partition_end_2")
        return head

    def Cut_link(self,listnode):
        cache = listnode.next
        listnode.next = listnode.next.next
        return cache 

def CreateListNode(l):
    head = ListNode(0)
    link = head
    for i in l:
        link.next = ListNode(i)
        link = link.next
    return head.next

def DecodeListNode(node):
    link = node
    data = []
    while link != None:
        data.append(link.val)
        link = link.next
    return data

if __name__ == "__main__":
    a = [1,4,3,2,5,2]
    head = CreateListNode(a)
    # print("end1")
    obj = Solution()
    head2 = obj.partition(head,3)
    # print("end2")
    ans = DecodeListNode(head2)
    print(ans)


