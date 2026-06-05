# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node1 = l1
        node2 = l2
        temp  = node1.val + node2.val
        car = temp // 10
        val = temp %10 
        res = ListNode(val)
        cur = res

        node1 = node1.next
        node2 = node2.next

        while node1 and node2 :
            temp  = node1.val + node2.val + car
            car = temp //10
            val = temp % 10
            cur.next = ListNode(val)
            cur = cur.next

            node1 = node1.next
            node2 = node2.next

        while node1:
            temp = node1.val + car
            car = temp // 10
            val = temp % 10

            cur.next = ListNode(val)
            cur = cur.next
            node1 = node1.next

        while node2:
            temp = node2.val + car
            car = temp // 10
            val = temp % 10

            cur.next = ListNode(val)
            cur = cur.next
            node2 = node2.next

        if car:
            cur.next = ListNode(car)
        return res




