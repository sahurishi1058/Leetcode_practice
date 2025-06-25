class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        total=0
        nums.sort()
        for i in range(0,n,2):
            total+=min(nums[i],nums[i+1])
        return total