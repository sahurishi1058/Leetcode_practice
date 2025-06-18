from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Below is the most optimal code for intersection but because of the requirement of the solution counter is to be used 
        # int_sol=[]
        # nums1=list(set(nums1))
        # nums2=list(set(nums2))
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i]==nums2[j] or nums2[j]==nums1[i]:
        #             int_sol.append(nums1[i])
                                        
        # return int_sol
        counts = Counter(nums1)
        result = []

        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1

        return result

