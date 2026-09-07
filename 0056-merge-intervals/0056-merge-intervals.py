class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        added = []
        a = intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][0]<= a[1]:
                a[1] = max(a[1],intervals[i][1])
            else:
                added.append(a)
                a = intervals[i]
        added.append(a)
        return added        