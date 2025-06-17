class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        sum_series=n*(n+1)//2
        actual_sum=sum(nums)
        return sum_series-actual_sum