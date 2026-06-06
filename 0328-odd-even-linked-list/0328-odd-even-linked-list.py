# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution(object):
#     def oddEvenList(self, head):
#         """
#         :type head: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         if not head:
#             return None

#         odd = ListNode(0)
#         even = ListNode(0)

#         o = odd
#         e = even

#         cur = head
#         i = 1

#         while cur  :
#             new = ListNode(cur.val)
#             if i % 2 != 0:
#                 o.next = new
#                 o = o.next
#             else:
#                 e.next = new
#                 e = e.next
#             cur = cur.next
#             i += 1

#         o.next = even.next
#         return odd.next




class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head

        return head