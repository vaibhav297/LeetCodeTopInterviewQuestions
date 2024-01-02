class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        sortedList= sorted(strs)

        firstString= sortedList[0]
        lastString= sortedList[-1]
        commonPrefix=""

        for x in range(len(min(firstString,lastString))):
            if firstString[x] == lastString[x]:
                commonPrefix+=firstString[x]
            else:
                break
        
        return commonPrefix
