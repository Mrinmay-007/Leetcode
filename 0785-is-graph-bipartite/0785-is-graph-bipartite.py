class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        v = len(graph)
        visited = [False]*v 
        color = [None]*v
    
        def bfs(start):
            
            Q = []
            Q.append(start)
            visited[start] = True
            color[start] = 'B'


            
            while len(Q) > 0:
                front = Q.pop(0)
                
                for x in graph[front]:
                    
                    if not visited[x]:
                        Q.append(x)
                        visited[x] = True
                        
                        if color[front] == 'B':
                            color[x] = 'W'
                        else:
                            color[x] ='B'
                            
                    elif color[front] == color[x]:
                        return False
                    
            return True
                    
                    
        for i in range(v):
            if not visited[i]:
                if not bfs(i):
                    return False

        return True
            
        