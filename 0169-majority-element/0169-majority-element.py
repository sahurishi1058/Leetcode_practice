class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj_ele=-1
        count=0
        for i in nums:
            if count==0:
                maj_ele=i
                count=1
            else:
                if maj_ele==i:
                    count+=1
                else:
                    count-=1
        return maj_ele
        