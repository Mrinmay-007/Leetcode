# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        diameter = [0]
        def dfs (node):

            if node is None :
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            diameter[0] = max(diameter[0], left + right)

            return max(left,right) +1
            
        dfs(root)

        return diameter[0] 


