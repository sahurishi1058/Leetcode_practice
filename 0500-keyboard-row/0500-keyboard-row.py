class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans=[]
        keyrows=["qwertyuiop","asdfghjkl","zxcvbnm"]
        for i in words:
            for j in keyrows:
                if all([x in j for x in i.lower()]):
                    ans.append(i)
        return ans
