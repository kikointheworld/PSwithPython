n, x =  map(int, input().split())
visits = list(map(int, input().split()))


sums = sum(visits[:x])
ans_sums = sum(visits[:x])
manys = 1

for i in range(x, n):
    sums = sums - visits[i - x] + visits[i]

    if ans_sums == sums:
        manys += 1
    elif sums > ans_sums:
        ans_sums = sums
        manys = 1

if sums == 0:
    print("SAD")
else:
    print(ans_sums)
    print(manys)
