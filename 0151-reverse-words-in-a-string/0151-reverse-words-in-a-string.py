class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        s = s.strip()
        s = s.split(" ")[::-1]

        for ch in s :
           
            if ch != "":
                res = res + ch + " " 

        res = res.strip()

        return res