class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n=len(grid)
        nums=n**2
        count=[0]*(nums+1)
        for i in range(n):
            for j in range(n):
                count[grid[i][j]]+=1
        a,b=-1,-1
        for i in range(1,nums+1):
            if count[i]==2:
                a=i
            if count[i]==0:
                b=i

        return [a,b]        
            