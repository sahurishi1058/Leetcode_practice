class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n=len(grid)
        rep=-1
        miss=-1
        currsum=0
        totalsum=((n*n)*((n*n)+1))//2
        for i in range(n):
            for j in range(n):
                val=abs(grid[i][j])
                row,col=divmod(val-1,n)
                if grid[row][col]<0:
                    rep=val
                grid[row][col]*=-1
                currsum+=val
        miss=totalsum-(currsum-rep)
        return [rep,miss]
        