class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        land,water,perimeter=len(grid),len(grid[0]),0
        for i in range(land):
            for j in range(water):
                if grid[i][j]:
                    perimeter+=4
                    if i and grid[i-1][j]:
                        perimeter-=2
                    if j and grid[i][j-1]:
                        perimeter-=2
        return perimeter
