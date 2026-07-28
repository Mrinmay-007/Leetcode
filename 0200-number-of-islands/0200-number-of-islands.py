class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        from collections import deque
        row = len(grid)
        col = len(grid[0])

        visited = [[False for _ in range(col)] for _ in range(row)]
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        count = 0

        for i in range (row):
            for j in range(col):
                if grid[i][j] == '1' and not visited[i][j]:
                    Q = deque()
                    Q.append((i,j))
                    visited[i][j] = True
                    
                    while Q:
                        
                        r , c = Q.popleft()
                        
                        for dr , dc in direction:
                            nr = r + dr
                            nc = c + dc
                            
                            if 0<= nr < row and  0<= nc < col :
                                if grid[nr][nc] == '1' and not visited[nr][nc]:
                                    Q.append((nr,nc))
                                    visited[nr][nc] = True
                                    
                    count +=1
        return count
