class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        if n == 1:
            return nums[0]

        def money(arr):
            def solve(i,memo={}):
                if i >= len(arr) :
                    return 0
                
                if i in memo :
                    return memo[i]

                take = arr[i] + solve(i+2,memo)
                skip = solve(i+1,memo)

                memo[i] = max(take,skip)

                return memo[i]

            return solve(0)

        case1  = money(nums[:-1])
        case2  = money(nums[1:])

        return max(case1,case2)

