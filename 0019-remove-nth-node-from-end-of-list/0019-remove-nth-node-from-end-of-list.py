class Solution(object):
    def removeNthFromEnd(self, head, n):
        # Step 1: find length
        temp = head
        m = 0
        while temp:
            m += 1
            temp = temp.next
        
        # Step 2: if we need to remove head
        if m == n:
            return head.next
        
        # Step 3: go to node just before the one to delete
        node = head
        for _ in range(m - n - 1):
            node = node.next
        
        # Step 4: delete node
        node.next = node.next.next
        
        return head