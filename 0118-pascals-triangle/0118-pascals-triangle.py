class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        prevs=self.generate(numRows-1)
        prev=prevs[-1]
        currRow=[1]
        for i in range(1,numRows-1):
            currRow.append(prev[i-1]+prev[i])
        currRow.append(1)
        prevs.append(currRow)
        return prevs
        
        
        