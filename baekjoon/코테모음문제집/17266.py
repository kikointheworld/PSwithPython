n = int(input())
m = int(input())
xs = list(map(int, input().split()))


ans = -1
if m == 1:
    ans = max(xs[0], n - xs[0])
else:
    gap = 0
    for i in range(len(xs) - 1):
        gap = max(gap, xs[i + 1] - xs[i])
    gap = gap // 2 if gap % 2 == 0 else (gap + 1) // 2
    ans = max(xs[0], n - xs[-1], gap)

print(ans)
