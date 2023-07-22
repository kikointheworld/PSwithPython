n, m = map(int ,input().split())

list1 = []

visited = [-1]

for _ in range(n):
    c, num = map(str, input().split())
    num = int(num)
    if visited[-1] == num:
        continue
    else:
        list1.append([num, c])

default_right = len(list1)

for _ in range(m):
    num = int(input())

    left = 0
    right = default_right

    while(left <= right):
        mid = (left + right) // 2
        if list1[mid][0] < num <= list1[mid + 1][0]:
            print(list1[mid])
            break

    for i in list1:
        if num <= i[0]:
            print(i[1])
            break
