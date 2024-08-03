def get_people(k, times):
    tmp = 0
    for time in times:
        tmp += k // time
    return tmp

def solution(n, times):
    ans = 999999999999999999999999
    times.sort()
    l = len(times)
    start = times[0] * (n // l)
    end = times[0] * n
    
    while(start <= end):
        
        mid = (start + end) // 2
        p = get_people(mid, times)
        
        if p >= n:
            ans = min(ans, mid)
            end = mid - 1
        elif p < n:
            start = mid + 1
    
    return ans


# 이분탐색을 떠올리는게 가장 중요할 듯. 
