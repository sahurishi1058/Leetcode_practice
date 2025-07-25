class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
        for j in range(n):
            k=n-1
            i=0
            while i<k:
                temp=matrix[j][i]
                matrix[j][i]=matrix[j][k]
                matrix[j][k]=temp
                i+=1
                k-=1