

n, new_score, p = map(int, input().split())
if n > 0:
    scores = list(map(int, input().split()))
else:
    print(1)
    exit(1)

left = 0
right = n - 1

# 맨 왼쪽에 박히면 될듯 ㅇㅇ

while(left < right):
    mid = (left + right) // 2
    if new_score > scores[mid]:
        right = mid
    else:
        left = mid + 1

print(left)

