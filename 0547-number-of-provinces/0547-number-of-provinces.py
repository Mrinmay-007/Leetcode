class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        v = len(isConnected)
        visited = [False]*v
        provinces = 0

        def dfs(i):

            visited[i] = True
            for x in range(v) :
                if isConnected[i][x] == 1 and not visited[x]:
                    dfs(x)
            
        for i in range(v):
            if not visited[i]:
                dfs(i)
                provinces +=1
        return provinces

