from collections import deque
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solution(rectangle, characterX, characterY, itemX, itemY):
    MAP = [[-1] * 103 for _ in range(103)]
    visited = [[0] * 103 for _ in range(103)]
    
    for r in rectangle:
        x1, y1, x2, y2 = r[0] * 2, r[1] * 2, r[2] * 2, r[3] * 2
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    MAP[j][i] = 0
                elif MAP[j][i] != 0:
                    MAP[j][i] = 1
  
    cx, cy, ix, iy = 2 * characterX, 2 * characterY, 2 * itemX, 2 * itemY
    q = deque()
    q.append((cy, cx, 0))
    visited[cy][cx] = 1
    while(q):
        y, x, cnt = q.popleft()
        if y == iy and x == ix:
            return cnt // 2
        for dy, dx in moves:
            ny, nx = y + dy, x + dx
            if  visited[ny][nx] == 0 and MAP[ny][nx] == 1:
                visited[ny][nx] = 1
                q.append((ny, nx, cnt + 1))
    
    
    return 0
