class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l1=set(nums)
        nums[:]=sorted(list(l1))
        j=len(nums)
        return j