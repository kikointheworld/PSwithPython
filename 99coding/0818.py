def solution(n, m, x, y, queries):
    answer = 0
    t, l, r, b = x, y, y, x
    queries.reverse()
    for i, j in queries:
        if i == 0:
            if r+j<m:
                tmp=r+j
            else:
                tmp=m-1
            if l == 0: 
                r = tmp
            else: 
                l, r = l + j, tmp
        if i == 1:
            if l-j>=0:
                tmp=l-j
            else:
                tmp=0
            if r == m - 1: 
                l = tmp
            else: 
                l, r = tmp, r - j
        if i == 2:
            if b+j<n:
                tmp=b+j
            else:
                tmp=n-1
            if t == 0:
                b = tmp
            else:
                t, b = t + j, tmp
        if i == 3:
            if t-j>=0:
                tmp=t-j
            else:
                tmp=0
            if b == n - 1:
                t = tmp
            else:
                t, b = tmp, b - j
        if l > m - 1 or r < 0 or t > n - 1 or b < 0:
            break
    else:
        answer = ((b - t) + 1) * ((r - l) + 1) 
    return answer
