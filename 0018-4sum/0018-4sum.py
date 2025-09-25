class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans=[]
        n=len(nums)
        nums.sort()
        for i in range(n):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            for j in range(i+1,n):
                if(j!=i+1 and nums[j]==nums[j-1]):
                    continue
                k=j+1
                l=n-1
                while k<l:
                    sum_tar=nums[i]
                    sum_tar+=nums[j]
                    sum_tar+=nums[k]
                    sum_tar+=nums[l]
                    if sum_tar==target:
                        ans.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1
                        while (k<l and nums[k]==nums[k-1]):
                            k+=1
                        while (k<l and nums[l]==nums[l+1]):
                            l-=1
                    elif sum_tar<target:
                        k+=1
                    else:
                        l-=1
        return ans
                        
        