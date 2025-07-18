class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals)<1:
            return intervals
        intervals.sort(key=lambda x: x[0])  # Step 1
        merged = [intervals[0]]             # Step 2

        for current in intervals[1:]:       # Step 3
            last = merged[-1]
            if current[0] <= last[1]:       # Overlap
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)

        return merged

