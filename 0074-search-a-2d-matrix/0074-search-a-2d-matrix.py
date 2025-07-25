class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        nums=[x for i in matrix for x in i]
        if target in nums:
            return True 
        else:
            return False