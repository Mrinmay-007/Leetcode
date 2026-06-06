# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        n= 0
        node = head
        while node :
            node = node.next
            n+=1
        
        mid = n//2
        node = head
        for _ in range(mid):
            node = node.next

        return node
                
        