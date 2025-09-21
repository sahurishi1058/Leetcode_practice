class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        lst=list([x for num in matrix for x in num])
        n=len(lst)
        def binary_search(lst,n,target):
            l=0
            h=n-1
            while l<=h:
                mid=(l+h)//2
                if target==lst[mid]:
                    return True
                elif target<lst[mid]:
                    h=mid-1
                else:
                    l=mid+1
            return False
        return binary_search(lst,n,target)
            

