class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums=list(set(nums))
        nums.sort()
        n=len(nums)
        maxlen = 1
        c = 1
        for i in range(n - 1):
            j = i + 1
            if nums[j] - nums[i] == 1:
                c += 1
                maxlen = max(maxlen, c)
            else:
                c = 1 # reset count if not consecutive
        return maxlen
