class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_vol=0
        n=len(height)
        i=0
        j=n-1
        while i<j:
            curr_vol=0
            h=min(height[i],height[j])
            w=j-i
            curr_vol=h*w
            if curr_vol>max_vol:
                max_vol=max(curr_vol,max_vol)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_vol