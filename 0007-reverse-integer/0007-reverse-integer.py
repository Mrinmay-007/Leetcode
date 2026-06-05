class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x < 0:
            x = x*-1
            res = str(x)
            res = res[::-1]
            res = int(res) * -1
        else:
            res = str(x)
            res = res[::-1]
            res = int(res)

        if res >= -2**31 and res <= 2**31 -1 :
            return res
        else:
            return 0

