class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n==0 and m==0:
            nums1=[]
        
        else:
            i=m
            j=m+n-1
            k=0
            while i<=j and k<n:

                nums1[i]=nums2[k]
                i+=1
                k+=1
            nums1.sort()




        