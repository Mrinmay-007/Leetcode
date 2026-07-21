class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs :
            return ""

        strs.sort()
        f = strs[0]
        l = strs[-1]

        i = 0 
        while i < len(f) and i < len(l):
            if f[i] != l[i]:
                break
            
            i+=1
        
        return f[:i]