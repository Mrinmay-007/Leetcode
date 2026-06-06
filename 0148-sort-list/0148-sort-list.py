# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # arr = []
        # cur = head

        # while cur :
        #     arr.append(cur.val)
        #     cur = cur.next
        # if len(arr) == 0:
        #     return None
        # Q = deque(sorted(arr))
        # res = ListNode(Q.popleft())
        # node = res
        # while Q :
        #     new = ListNode(Q.popleft())
        #     node.next = new
        #     node = node.next
        # return res

# Method 2 ==================
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        arr.sort()
        temp = head
        i = 0
        while temp:
            temp.val = arr[i]
            i += 1
            temp = temp.next
        return head

        

        