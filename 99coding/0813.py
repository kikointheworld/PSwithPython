import heapq as hq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        l = len(profits)
        p_c_pairs = []
        for i in range(l):
            hq.heappush(p_c_pairs, (capital[i], profits[i]))
        hq_list = []

        while(k):
            while(p_c_pairs):
                c, profit = hq.heappop(p_c_pairs)
                if c > w:
                    hq.heappush(p_c_pairs, (c, profit))
                    break
                hq.heappush(hq_list, -1 * profit)
            
            if hq_list:
                profit = hq.heappop(hq_list)
                w -= profit
            else:
                break

            k -= 1

        return w
        
