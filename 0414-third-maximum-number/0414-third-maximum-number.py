class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)>=3:
            nums=list(set(nums))
            max1=max(nums)
            nums.remove(max1)
            max2=max(nums)
            nums.remove(max2)
            return max(nums)
        else:
            return max(nums)