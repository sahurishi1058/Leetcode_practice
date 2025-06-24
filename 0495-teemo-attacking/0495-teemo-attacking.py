class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        timer=0
        k=0
        for i in range(len(timeSeries)):
            j=timeSeries[i]
            while(j<(timeSeries[i]+duration)):
                if i<len(timeSeries)-1 and j>=timeSeries[i+1]:
                    break
                timer+=1
                j+=1
                
        return timer
        