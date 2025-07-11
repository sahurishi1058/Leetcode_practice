class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]>nums[j]:
                    for k in range(j,i,-1):
                        nums[k],nums[k-1]=nums[k-1],nums[k]
        