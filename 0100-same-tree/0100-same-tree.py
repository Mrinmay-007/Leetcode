# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        self.res1 = []
        self.res2 = []


        def dfs(node,res = []):
            if node is None :
                res.append("null")
                return 
            # if node.val == None :
            #     res.append('null')
            # else:
            res.append(node.val)
            dfs(node.left,res)
            dfs(node.right,res)
            return res
        
        dfs(p,self.res1)
        dfs(q,self.res2)


        return  self.res1 ==  self.res2

        