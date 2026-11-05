class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0])
        row_zeros=[]
        col_zeros=[]
        for i in range(0,row):
            for j in range(0,col):
                if matrix[i][j]==0:
                    if i not in row_zeros: 
                        row_zeros.append(i)
                    if j not in col_zeros:
                        col_zeros.append(j)
                else:
                    continue
        for i in col_zeros:
            for j in range(row):
                matrix[j][i]=0
        for i in row_zeros:
            for j in range(col):
                matrix[i][j]=0

        