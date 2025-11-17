class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        nums.sort()
        ans=[]
        for i in range(n):
            target=0-nums[i]
            start=i+1
            end=n-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while start<end:
                currsum=nums[start]+nums[end]
                if currsum==target:
                    ans.append([nums[i],nums[start],nums[end]])
                    start+=1
                    end-=1
                    while start<end and nums[start]==nums[start-1]:
                        start+=1
                    while start<end and nums[end]==nums[end+1]:
                        end-=1
                elif currsum<target:
                    start+=1
                else:
                    end-=1
        return ans

