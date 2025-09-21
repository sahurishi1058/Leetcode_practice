from collections import Counter
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=Counter(nums)
        for num,count in x.items():
            if count>1:
                return num
