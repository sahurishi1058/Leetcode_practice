class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        ans=""
        if n>2:
            for i in range(n):
                for j in range(i+1,n+1):
                    sub=s[i:j]
                    if sub==sub[::-1] and len(sub)>len(ans):
                        ans=sub
                    else:
                        continue
            return ans
        elif n==2:
            if s==s[::-1]:
                return s
            else:
                return s[0]
        else:
            return s