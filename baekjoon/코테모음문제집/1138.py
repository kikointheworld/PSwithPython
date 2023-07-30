n = int(input())

lists = list(map(int, input().split()))

d = [0] * (n)

for i in range(0, n):
    zero_cnt = lists[i]
    for j in range(0, n):
        if zero_cnt == 0:
            if d[j] == 0:
                d[j] = i+1
                break
            else:
                continue
        if d[j] == 0:
            zero_cnt -= 1



for i in range(n):
    print(d[i], end = ' ')