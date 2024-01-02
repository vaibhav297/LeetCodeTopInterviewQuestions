class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsRange = all (no>=-10**9 and no<=10**9 for no in nums) and len(nums)>=2 and len(nums)<=10**4
        targetRange= target>=-10**9 and target <=10**9
        if numsRange and targetRange:
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if nums[i]+nums[j] == target:
                        return [i,j]
