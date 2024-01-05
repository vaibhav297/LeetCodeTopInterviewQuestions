class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        solved using binary search
        """
        left=1
        right=x

        while (left<right):
            mid = (left+right)/2
            temp= x/mid

            if(temp== mid):
                return temp

            elif(temp<mid):
                right= mid
            else:
                left= mid+1
        
        if left>1:
            return left-1
        else:
            return x
