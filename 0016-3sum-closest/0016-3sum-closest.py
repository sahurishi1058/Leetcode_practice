class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans =[]
        nums.sort()
        n=len(nums)
        closest=float('inf')
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=n-1
            while l<r :
                total=nums[i]+nums[l]+nums[r]
                if abs(target-total)<abs(target-closest):
                    closest=total
                elif total<target:
                    l+=1
                elif total>target:
                    r-=1
                else:
                    return total
        return closest