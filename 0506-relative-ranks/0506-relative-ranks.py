class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        
        st={}
        s1=sorted(score,reverse=True)
        for i in range(len(s1)):
            if i==0:
                st[s1[i]]="Gold Medal"
            elif i==1:
                st[s1[i]]="Silver Medal"
            elif i==2:
                st[s1[i]]="Bronze Medal"
            else:
                st[s1[i]]=str(i+1)
        ans=[st[i] for i in score]
        return ans
        