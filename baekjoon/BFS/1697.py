'''
https://www.acmicpc.net/problem/1697
'''

from collections import deque

n, k = map(int, input().split())



def bfs(x):
    q = deque([[x, 0]])

    while q:
        tmp = q.popleft()
        position = tmp[0]
        ans = tmp[1]
        if position < 0  or position >= 100001:
            continue

        if isVisited[position] == 1:
            continue

        if position == k:
            print(ans)
            return
            

        isVisited[position] = 1
        

        
        q.append([position * 2, ans + 1])
        q.append([position + 1, ans + 1])
        q.append([position - 1, ans + 1])
        

isVisited = [0] * 100002

bfs(n)
