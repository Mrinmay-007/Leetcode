class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = nums1 + nums2
        merged.sort()
        n = len(merged)
        
        if n % 2 == 0:
            i = n//2
            j = i-1
            return (merged[i] + merged[j]) /2.0
        else:
            i = n//2
            return merged[i]
