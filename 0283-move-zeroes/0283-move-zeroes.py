class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a,b=0,0
        while(a<len(nums)):
            if nums[a]!=0:
                nums[a],nums[b]=nums[b],nums[a]
                b+=1
            a+=1
                
        
        