# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        self.lvl  = 0

        def bfs (node):
            if node is None :
                return []
            
            q = [node]
            res = []

            while q :
                level = []
                lvl_size = len(q)

                for _ in range(lvl_size) :
                    front = q.pop(0)
                    level.append(front.val)

                    if front.left :
                        q.append(front.left)
                    if front.right :
                        q.append(front.right)

                if self.lvl % 2 != 0 :
                    res.append(level[::-1])
                else:
                    res.append(level)
                
                self.lvl +=1
            return res

        res = bfs(root)
        return res


        