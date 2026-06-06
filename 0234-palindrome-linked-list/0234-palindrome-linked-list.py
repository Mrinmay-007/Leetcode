# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        arr = []
        node = head 
        while node:
            val = node.val
            arr.append(val)
            node = node.next
        return arr == arr[::-1]
        