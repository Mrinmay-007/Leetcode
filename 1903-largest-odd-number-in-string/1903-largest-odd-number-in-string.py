class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        odd = '13579'
        res = ""
        n = len(num)
        for i in range(n-1,-1,-1):
            if num[i] in odd :
                break
        if i >= 0 and num[i] in odd :
            res += num[:i+1]
        return res