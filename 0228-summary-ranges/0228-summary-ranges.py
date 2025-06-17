class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans=[]
        a=nums[0]
        b=nums[0]
        for i in nums[1:]:
            if i==b+1:
                b=i
            else:
                if a==b:
                    ans.append(str(a))
                else:
                    ans.append(str(a)+"->"+str(b))
                a=i
                b=i
        if a==b:
            ans.append(str(a))
        else:
            ans.append(str(a)+"->"+str(b))
        return ans
                