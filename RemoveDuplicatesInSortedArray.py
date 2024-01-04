class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i=0
        j=1
        while j< len(nums):
            if nums[j] not in nums[0:i+1]:
                nums[i+1]= nums[j]
                i+=1
            j+=1
        
        return i+1
