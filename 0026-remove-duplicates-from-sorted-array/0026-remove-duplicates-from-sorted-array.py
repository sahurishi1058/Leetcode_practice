class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=set(nums)
        nums[:]=sorted(list(l))
        j=len(nums)
        return j