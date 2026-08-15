class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0])
        row_zeros=[]
        col_zeroes=[]
        for i in range(row) :
            for j in range(col):
                if matrix[i][j]==0 :
                    if i not in row_zeros:
                        row_zeros.append(i)
                    if  j not in col_zeroes:
                        col_zeroes.append(j)
        for j in range(col):
                for a in row_zeros:
                    matrix[a][j]=0
        for i in range(row) :
                for b in col_zeroes:
                    matrix[i][b]=0