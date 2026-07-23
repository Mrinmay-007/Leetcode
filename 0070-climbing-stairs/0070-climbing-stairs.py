class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # memoization
        def dp_memo(n,memo ={}):
            if n <= 2 :
                return n

            if n in memo :
                return n

            memo [n] = dp_memo(n-1,memo) + dp_memo(n-2,memo)
            return memo[n]

        # tabulation
        def dp_tab(n):
            if n <= 2 :
                return n

            dp = [0] * (n+1)
            dp[1],dp[2] = 1 , 2

            for i in range(3,n+1):
                dp[i] = dp[i-1] + dp[i-2]
            return dp[n]
        
        return  dp_tab(n)
