class Solution(object):

    def max_sub_array(self,arr,k):
        l =0
        ans = 0
        odd = 0

        for r in range(len(arr)):
            if arr[r] % 2 != 0:
                odd +=1
            
            while odd > k :
                if arr[l] %2 != 0 :
                    odd -=1
                l+=1
            ans += r - l +1
        return ans



    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        kth = self.max_sub_array(nums,k)
        kth_1 = self.max_sub_array(nums,k-1)
        return kth - kth_1
      