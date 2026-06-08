# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or k== 1 :
            return head

        cur = head
        new_head = None
        prev_tail = None

        while cur :
            n = k
            temp = cur
            
            # step 1 : Count whether k nodes exist
            
            for _ in range(k):
                if temp is None:
                    break
                temp = temp.next
                n -= 1
            
            # step 2 : Reverse the first k nodes
            if n == 0 :
                prev = temp 
                tail = cur
                
                while n < k:
                    nxt = cur.next
                    cur.next = prev
                    prev = cur
                    cur = nxt
                    n+=1

                if new_head is None :
                    new_head = prev

                if prev_tail :
                    prev_tail.next = prev

                prev_tail = tail
            else:
                break

        return new_head if new_head else head




