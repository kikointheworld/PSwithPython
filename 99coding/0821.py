class Solution(object):
    def minOperations(self, target, arr):
        d  = {n : i for i, n in enumerate(target)}
        # print(d)
        def LIS(arr):
            LIS = []
            for cnt, n in enumerate(arr):
                if n in d:
                    i = bisect_left(LIS, d[n])
                    if i == len(LIS):
                        LIS.append(d[n])
                    else:
                        LIS[i] = d[n]
                # print(cnt, LIS)
            return len(LIS)
        return len(target) - LIS(arr)
