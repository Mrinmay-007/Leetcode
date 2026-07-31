# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
  
        self.prev = None

        def dfs(node):
            if node is None :
                return True
            
            if not dfs(node.left) :
                return False
            
            if  self.prev is not None and node.val <= self.prev:
                return False
            
            self.prev = node.val

            return dfs(node.right)
        
        return dfs(root)

       
        