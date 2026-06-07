# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        
        temp = head 
        n = 0
        while temp :
            n+=1
            temp = temp.next
        
        if not head or not head.next:
            return head


        list1 = ListNode(0)
        list2 = ListNode(0)
        l1 , l2 = list1 , list2

        temp = head

        k = k % n
        m = n - k
        i = 0
        if k == 0:
            return head

        while temp:
            node = ListNode(temp.val)
            if i < m :
                l2.next = node
                l2 =l2.next
            else:
                l1.next = node
                l1 =l1.next
            i+=1
            temp =temp.next
        
        l1.next = list2.next
        return list1.next




