class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        res = ""
        d = 0

        for ch in s :
            if ch == "(" :
                if d > 0 :
                    res +=ch
                d+=1
            
            else :
                d-=1
                if d > 0:
                    res+=ch
        return res 