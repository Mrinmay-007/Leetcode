# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def dfs(node):
            if not node:
                return (0, None)
            
            left_height , left_lca = dfs(node.left)
            right_height , right_lca = dfs(node.right)

            if left_height > right_height :
                return (left_height + 1, left_lca)
            
            if left_height < right_height :
                return (right_height + 1, right_lca)
            
            return (right_height  + 1 , node)

        return dfs(root)[1]

