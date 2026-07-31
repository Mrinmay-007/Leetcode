# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        Q = [root]
        seen_null = False
        while Q:
            node = Q.pop(0)
            if node is None:
                seen_null = True

            else:
                if seen_null:
                    return False

                Q.append(node.left)
                Q.append(node.right)
            
        return True
        