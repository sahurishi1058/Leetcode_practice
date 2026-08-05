class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """        
        word=s.split()
        rev_word=word[::-1]
        s=' '.join(rev_word)
        return s