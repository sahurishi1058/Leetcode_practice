class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1=list(set(nums1))
        nums2=list(set(nums2))
        int_arr=[]
        for x in nums1[:]:
            if x in nums2[:]:
                int_arr.append(x)
            else:
                continue
        return int_arr
