class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
       
        if len(set(s)) != len(set(t)) :
            return False
            
        n = len(s)
      
        d = {}

        for i in range(n):
            if s[i] not in d :
                d[s[i]] = t[i]
            
            else: 
                if d[s[i]] != t[i]:
                    return False
        return True