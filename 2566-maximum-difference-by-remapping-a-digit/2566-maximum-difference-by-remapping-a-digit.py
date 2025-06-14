class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        st=str(num)
        k=''
        m=''
        for i in st:
            if i!='9':
                k=i
                break
        max_num=''.join(['9' if i==k else i for i in st])
        m=st[0]
        min_num=''.join(['0' if i==m else i for i in st ])

        return int(max_num)-int(min_num)