class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def twosum(nums1,target1):
            n=len(nums1)
            start=0
            end=n-1
            ans=[]
            while start<end:
                currsum=nums1[start]+nums1[end]
                if currsum==target1:    
                    ans.append([nums1[start], nums1[end]])
                    start += 1
                    end -= 1
                    while start < end and nums1[start] == nums1[start - 1]:
                        start += 1
                    while start < end and nums1[end] == nums1[end + 1]:
                        end -= 1
                elif currsum > target1:
                    end -= 1
                else:
                    start += 1
            return ans

        nums.sort()
        n=len(nums)
        ans=[]
        for i in range(n-3):
            a=nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                b = nums[j]
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                t1 = target - a - b
                k = twosum(nums[j + 1:], t1)
                for pair in k:
                    ans.append([a, b] + pair)
        return ans

           