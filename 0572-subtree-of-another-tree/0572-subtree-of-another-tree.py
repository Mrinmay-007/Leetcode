# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def same_tree(p,q):
            if not p and not q :
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False

            return(
                same_tree(p.left,q.left)
                and
                same_tree(p.right,q.right)
            )

        def dfs(node):

            if node is None :
                return False
            
            if same_tree(node,subRoot):
                return True
            
            return(
                dfs(node.left)
                or
                dfs(node.right)
            )
        
        return dfs(root)    
    



        
