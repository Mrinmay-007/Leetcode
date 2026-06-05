class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n =len(height)
        l = 0
        r = n -1
        maxi = 0
        
        while l < r:
            left = height[l]
            right = height[r]

            h = min(left,right)
            width = r - l
            area = width*h
            maxi = max(maxi,area)

            if left < right :
                l+=1
            else:
                r -=1
        return maxi
