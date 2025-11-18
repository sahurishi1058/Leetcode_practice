class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        try:
            k=nums.index(target)
            lst=len(nums)-1-(nums[::-1].index(target))
            return [k,lst]
        except Exception as e:
                return [-1,-1]