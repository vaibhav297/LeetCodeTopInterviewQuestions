class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i=0
     
        needleLen = len(needle)
        if needle in haystack:
            while i<len(haystack):
                if haystack[i]==needle[0] and len(haystack[i:])>=needleLen:
                    if  haystack[i:i+needleLen] == needle[0:]:
                        return i
                i+=1
        else:
            return -1
