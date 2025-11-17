class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        nums.sort()
        ans=0
        max_diff=float('inf')
        c_sum=0
        for i in range(n):
            start=i+1
            end=n-1
            while start<end:
                currsum=nums[i]+nums[start]+nums[end]
                diff=abs(target-currsum)
                if diff<max_diff:
                    max_diff=diff
                    c_sum=currsum
                if currsum<target:
                    start+=1
                elif currsum>target:
                    end-=1
                else:
                    return currsum
        return c_sum
                    