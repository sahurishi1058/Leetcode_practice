class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d=dict()
        d={0:1}
        cnt=0
        pref_sum=0
        for i in range(len(nums)):
            pref_sum+=nums[i]
            rem=pref_sum-k
            cnt+=d.get(rem,0)
            d[pref_sum]=d.get(pref_sum,0)+1
        return cnt
        
        