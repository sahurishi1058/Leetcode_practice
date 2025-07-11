import sys
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start=0
        end=0
        currSum=0
        maxSum=-sys.maxsize-1
        n=len(nums)
        while end<n:
            while currSum<0:
                currSum-=nums[start]
                start+=1
            currSum+=nums[end]
            end+=1
            maxSum=max(currSum,maxSum)
        return maxSum