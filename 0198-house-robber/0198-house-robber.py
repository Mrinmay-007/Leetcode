class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
    
        def money(i,memo={}): 
            if i >= n :
                return 0
            
            if i in memo:
                return memo[i]
                
            take = max(
                nums[i] + money(i+2,memo),
                money(i+1,memo)
                )
            skip = money(i+1,memo)
            
            memo[i]= max(take,skip)
            return memo[i]

        return money(0)
        