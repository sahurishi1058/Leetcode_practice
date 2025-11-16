class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp=nums.copy()
        nums.sort()
        n=len(nums)
        start=0
        end=n-1
        while start<end:
            currsum=nums[start]+nums[end]
            if currsum==target:
                ans=[]
                for i in range(n):
                    if nums[start]==temp[i] or temp[i]==nums[end]:
                        ans.append(i)
                return ans 
            elif currsum<target:
                start+=1
            else:
                end-=1
        return -1
        