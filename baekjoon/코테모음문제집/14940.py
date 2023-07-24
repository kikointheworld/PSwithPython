from collections import deque
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def in_map(y, x):
    if 0 <= y < n and 0 <= x < m:
        return True
    return False

n, m = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if MAP[i][j] == 2:
            start_y, start_x = i, j

q = deque()
q.append((start_y, start_x, 0))
visited[start_y][start_x] = 1
MAP[start_y][start_x] = 0

while(q):
    y, x, distance = q.popleft()

    for dy, dx in move:
        ny, nx = y + dy, x + dx
        if in_map(ny, nx) and not visited[ny][nx] and MAP[ny][nx] != 0:
            MAP[ny][nx] = distance + 1
            visited[ny][nx] = 1
            q.append((ny, nx, distance + 1))

for i in range(n):
    for j in range(m):
        if visited[i][j]:
            print(MAP[i][j], end = ' ')
        else:
            if MAP[i][j] == 1:
                print(-1, end = ' ')
            else:
                print(MAP[i][j], end = ' ')
    print()
                                        

