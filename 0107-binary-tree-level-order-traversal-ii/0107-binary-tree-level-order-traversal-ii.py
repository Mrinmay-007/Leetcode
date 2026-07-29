# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        
        if root is None:
            return []
        res = []
        Q = [root]

        while Q:
            size  = len(Q)
            lvl = []
            for _ in range(size):
                node = Q.pop(0)
                lvl.append(node.val)

                if node.left :
                    Q.append(node.left)
                if node.right :
                    Q.append(node.right)
            res.append(lvl)
                
        return res[::-1]
        