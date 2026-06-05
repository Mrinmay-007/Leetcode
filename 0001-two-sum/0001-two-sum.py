class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        seen = {}
        for i in range(len(nums)):
            ch = nums[i]
            temp = target - ch
            if temp in seen :
                return [seen[temp],i]
            seen[ch] = i
