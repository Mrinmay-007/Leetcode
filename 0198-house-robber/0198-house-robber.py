class Solution(object):
    def rob(self, nums):
        n = len(nums)

        def solve(i, memo={}):
            if i >= n:
                return 0

            if i in memo:
                return memo[i]

            take = nums[i] + solve(i + 2, memo)
            skip = solve(i + 1, memo)

            memo[i] = max(take, skip)
            return memo[i]

        return solve(0)