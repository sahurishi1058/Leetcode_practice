class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        ans=[]
        c=0
        g.sort()
        s.sort()
        if not (g and s):
            return 0
        else:
            i,j=0,0
            while i<len(g) and j<len(s):
                if s[j]>=g[i]:
                    c+=1
                    i+=1
                j+=1
            return c