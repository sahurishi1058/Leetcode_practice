class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans=[[1]]
        for i in range(numRows-1):
            temp=[0]+ans[-1]+[0]
            rows=[]
            for j in range(len(ans[-1])+1):
                rows.append(temp[j]+temp[j+1])
            ans.append(rows)
        return ans
        