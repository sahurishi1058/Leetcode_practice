class Solution(object):
        def majorityElement(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            n=len(nums)
            maj_ele1=None
            maj_ele2=None
            count1=0
            count2=0
            if not nums:
                return []
            for i in nums:
                if maj_ele1==i:
                    count1+=1                    
                elif maj_ele2==i:
                    count2+=1                   
                elif count1==0:
                    maj_ele1=i
                    count1=1                        
                elif count2==0:
                    maj_ele2=i
                    count2=1
                else:    
                    count1-=1
                    count2-=1
            count1=0
            count2=0
            maj_arr=[]
            for i in nums:
                if maj_ele1==i:
                    count1+=1
                elif maj_ele2==i:
                    count2+=1
                
            if count1>(n//3):
                    maj_arr.append(maj_ele1)
            if count2>(n//3):
                    maj_arr.append(maj_ele2)
            
            return maj_arr
            

        