# 2:42


# 홀수 row , 짝수 row 를 기준으로, 붙어있는 벽면을 생각
# 홀수 row 일 경우, x, x + 1이 붙고.
# 짝수 row 일 경우, x - 1, x 가 붙는다. 
# 여기서 밖인 부분과 안쪽 부분은 어떻게 구별할 것인가?

# 이를 확인하는 직관적인 방법은, 내부의 흰 부분부터 스타트해서 모든 면이 검은 색인지 아닌지 찾는 것임.

# 먼저 색칠 된 것부터 확인하고 그 이후에 색칠 안 된것 체크하는게 좋아보인다. 

import sys
from collections import deque

odd_moves = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0)]
even_moves = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1)]

def input():
    return sys.stdin.readline().rstrip()

def in_map(y, x):
    return 0 <= y < n and 0 <= x < m

def one_bfs(start_y, start_x):
    visited[start_y][start_x] = 1
    q = deque()
    q.append((start_y, start_x))
    cnt = 0
    while(q):
        y, x = q.popleft()
        cnt += 6
        moves = even_moves if y % 2 == 0 else odd_moves
        for dy, dx in moves:
            ny, nx = y + dy, x + dx
            if not in_map(ny, nx):
                continue
            if MAP[ny][nx] == 1:
                if visited[ny][nx]:
                    cnt -= 1
                else:
                    visited[ny][nx] = 1
                    cnt -= 1
                    q.append((ny, nx))

    return cnt


def zero_bfs(start_y, start_x):
    visited[start_y][start_x] = 1
    q = deque()
    q.append((start_y, start_x))
    cnt = 0
    flag = True
    while(q):
        y, x = q.popleft()
        moves = even_moves if y % 2 == 0 else odd_moves
        for dy, dx in moves:
            ny, nx = y + dy, x + dx
            if not in_map(ny,nx):
                flag = False
                continue
            if MAP[ny][nx] == 1:
                cnt += 1
            else:
                if not visited[ny][nx]:
                    visited[ny][nx] = 1
                    q.append((ny,nx))


    return cnt if flag else 0


m, n = map(int, input().split())
ans = 0
MAP = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
for y in range(n):
    for x in range(m):
        if not visited[y][x] and MAP[y][x] == 1:
            ans += one_bfs(y, x)


for y in range(n):
    for x in range(m):
        if not visited[y][x] and MAP[y][x] == 0:
            ans -= zero_bfs(y, x)

print(ans)
