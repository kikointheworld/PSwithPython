'''
https://www.acmicpc.net/problem/2178
'''


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(a, b):
    if graph[a][b] == 0:
        return

    graph[a][b] = 0
    ans_list[-1] += 1
    

    for i in range(4):
        tmp_x = a + dx[i]
        tmp_y = b + dy[i]

        if tmp_x < 0 or tmp_x >= n or tmp_y < 0 or tmp_y >= n:
            continue
        dfs(tmp_x, tmp_y)
    

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

ans_list = []


for q in range(n):
    for w in range(n):
        if graph[q][w] == 1:
            ans_list.append(0)
            dfs(q, w)



print(len(ans_list))
ans_list.sort()
for answer in ans_list:
    print(answer)
