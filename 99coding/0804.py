def is_possible(rocks, l, n, mid):
    erase_cnt = 0
    start = 0
    for i in range(l):
        if rocks[i] - start >= mid:
            start = rocks[i]
        else:
            erase_cnt += 1
    
    if erase_cnt > n:
        return False
    return True

def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    l = len(rocks)
    answer = 0
    
    start = 0
    end = rocks[-1]
    
    while(start <= end):
        mid = (start + end) // 2
        flag = is_possible(rocks, l, n, mid)
        if flag:
            start = mid + 1
        else:
            end = mid - 1
    
    return end 



# end가 가능한 거리의 최댓값이 되니까, return end 로 해야함.
