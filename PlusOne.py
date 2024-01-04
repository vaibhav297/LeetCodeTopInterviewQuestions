class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit=""
        for x in range(len(digits)):
            digit=digit+str(digits[x])
        
        digit= str(int(digit)+1)
        digitList= list(map(int, digit))

        return digitList
