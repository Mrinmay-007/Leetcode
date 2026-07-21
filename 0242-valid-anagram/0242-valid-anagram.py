class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list = list(s)  
        t_list = list(t)
        if sorted(s_list) == sorted(t_list) :
            return True
        return False