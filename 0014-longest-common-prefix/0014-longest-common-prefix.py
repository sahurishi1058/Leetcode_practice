class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        l=strs[0]
        for x in strs[1:]:
                while not x.startswith(l):
                    l=l[:-1]
                    if not l :
                        return ""
                    
        return l

       