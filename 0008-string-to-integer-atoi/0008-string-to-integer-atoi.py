class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()

        nums = '0123456789'
        res = "0"
        neg = False
        if len(s) == 0:
            return 0
        if s[0] == '-':
            neg = True
            s= s[1:] 
        elif s[0] == '+':
            s= s[1:] 
        
        for ch in s :
            if ch in nums :
                res+=ch
            else:
                break
        res = int(res)
        if neg:
            res = res * -1
        if res >= -2 ** 31 and res <= 2**31 -1:
            return res
        elif res <= -2 ** 31 :
            return -2 ** 31
        elif res >= 2**31 - 1:
            return 2 ** 31 -1
