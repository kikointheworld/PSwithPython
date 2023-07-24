import sys

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    n = int(input())
    days = list(map(int, input().rstrip().split()))

    # d = [0] * n
    now_max = days[-1]

    ans = 0
    for i in range(n - 2, -1, -1):
        if days[i] < now_max:
            ans += now_max - days[i]
        elif days[i] > now_max:
            now_max = days[i]


    print(ans)
