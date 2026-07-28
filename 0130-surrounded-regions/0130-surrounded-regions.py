class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        from collections import deque

        row = len(board)
        col = len(board[0])
        visited = [[False for _ in range(col)] for _ in range(row)]
        Q = deque()

        for i in range(row):
            if board[i][0] == 'O':
                Q.append((i,0))
                visited[i][0] = True
            
            if board[i][col - 1] == 'O':
                Q.append((i,col-1))
                visited[i][col - 1] = True
                
        for i in range(col):
            if board[0][i] == 'O':
                Q.append((0,i))
                visited[0][i] = True
            
            if board[row-1][i] == 'O':
                Q.append((row -1,i))
                visited[row -1][i] = True
                

        direction = [(1,0),(-1,0),(0,1),(0,-1)]


        while Q :
            r,c = Q.popleft()
            
            for dr,dc in direction :
                nr = dr + r
                nc = dc + c
                
                if 0 <= nr < row and 0 <= nc < col :
                    if not visited[nr][nc] and board[nr][nc] == 'O':
                        visited[nr][nc] = True
                        Q.append((nr,nc))
                        
        for i in range(row):
            for j in range(col):
                
                if not visited[i][j] and board[i][j] == 'O':
                    board[i][j] = 'X'

        return board 