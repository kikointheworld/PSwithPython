import sys
input = sys.stdin.readline

n = int(input().rstrip())

tmp_list = []


max_a = 0
max_b = 0
for i in range(n):
    a, b = map(int, input().rstrip().split())
    tmp_list.append([a, b])
    if b > max_b:
        max_a = a
        max_b = b
# d = [0] * ( + 1)

tmp_list.sort(key = lambda x : x[0])

ans = 0

target = 0

x = tmp_list[0][0]
y = tmp_list[0][1]

for i in range(1, n):
    if max_a == tmp_list[i][0]:
        ans += (tmp_list[i][0] - x) * y
        break

    if y < tmp_list[i][1]:
        ans += (tmp_list[i][0] - x) * y
        y = tmp_list[i][1]
        x = tmp_list[i][0]


x = tmp_list[-1][0]
y = tmp_list[-1][1]

for i in range(n - 2, -1, -1):
    if max_a == tmp_list[i][0]:
        ans += (x - tmp_list[i][0]) * y
        break
    if y < tmp_list[i][1]:
        ans += (x - tmp_list[i][0]) * y
        x = tmp_list[i][0]
        y = tmp_list[i][1]


print(ans + max_b)