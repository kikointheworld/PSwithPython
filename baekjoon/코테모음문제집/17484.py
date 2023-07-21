from collections import deque

move = [(1, -1), (1, 0), (1, 1)]


def in_map(y, x):
    if 0 <= y < n and 0 <= x < m:
        return True
    else:
        return False

n, m = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(n)]

ans = 999999999
q = deque()
for i in range(m):
    for j in range(3):
        q.append((0, i, MAP[0][i], j))

while(q):
    now_y, now_x, value, previous_move = q.popleft()

    for i in range(3):
        if i == previous_move:
            continue
        dy, dx = move[i][0], move[i][1]
        new_y, new_x = now_y + dy, now_x + dx
        if in_map(new_y, new_x):
            new_value = value + MAP[new_y][new_x]
            if new_y == n - 1:
                ans = min(ans, new_value)
            else:
                q.append((new_y, new_x, new_value, i))

print(ans)

    
