class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen=set()
        i=0
        max_len=0
        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i+=1
            seen.add(s[j])
            max_len=max(max_len,j-i+1)
        return max_len