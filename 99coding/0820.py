import heapq as hq

class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        l = len(startTime)
        jobs = []
        for i in range(l):
            jobs.append((startTime[i], endTime[i], profit[i]))
        jobs.sort(key = lambda x : x[0])

        q = []
        ans = 0
        current = 0
        for s, e, p in jobs:

            while(q and q[0][0] <= s):
                _, now_p = hq.heappop(q)
                current = max(current, now_p)
            
            hq.heappush(q, (e, current + p))
            ans = max(ans, current + p)

        return ans



            
        
