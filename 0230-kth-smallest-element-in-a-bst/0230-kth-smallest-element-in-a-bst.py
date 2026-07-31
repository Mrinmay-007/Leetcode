# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        self.count = 0
        def dfs(node):

            if node is None :
                return None
            
            left = dfs(node.left)
            if left is not None:
                return left

            self.count +=1
            if  self.count == k :
                return node.val

            return dfs(node.right)
            
        return dfs(root)

