# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):
#     def lowestCommonAncestor(self, root, p, q):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: TreeNode
#         """
#         self.ans = None 

#         def dfs(node):
#             if node is None :
#                 return 0
            
#             left = dfs(node.left)
#             right = dfs(node.right)
#             own = 0

#             if (node == p or node == q):
#                 own = 1
#             total = left + right + own 

#             if total == 2 and self.ans  is None :
#                 self.ans = node

#             return  total

#         dfs(root)
#         return self.ans       


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        elif left:
            return left
        else:
            return right