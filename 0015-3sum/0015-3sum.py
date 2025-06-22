class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if i!=j and i!=k and j!=k:
                        sum_tar=nums[i]+nums[j]+nums[k]
                        if sum_tar==0:
                            pair=sorted([nums[i],nums[j],nums[k]])
                            if pair not in ans:
                                ans.append(pair)
                        
        return ans

