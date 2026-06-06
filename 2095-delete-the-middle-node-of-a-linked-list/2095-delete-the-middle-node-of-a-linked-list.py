# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = head
        n = 0
        while cur :
            cur =cur.next
            n+=1
        
        mid = n//2
        i = 0
        node = head
        
        if mid == 0:
            return None

        while node :
            if i == mid-1 :
                node.next = node.next.next
                break

            node = node.next
            i+=1
        return head

