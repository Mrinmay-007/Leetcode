from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        q = deque()
        fresh = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2 :
                    q.append((i,j))
                elif grid[i][j] ==1:
                    fresh +=1
        

        minutes = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q and fresh > 0:

            size = len(q)

            for _ in range(size):
                r , c = q.popleft()
                for dr , dc in directions:

                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < row and 0 <= nc < col: 
                        if grid[nr][nc] == 1 :
                            grid[nr][nc] = 2
                            fresh -=1
                            q.append((nr,nc))

            minutes +=1
        
        if fresh == 0 :
            return minutes
        return -1
        
            





            


  
       

       

                


