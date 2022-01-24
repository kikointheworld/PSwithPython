# BFS (Breadth-First-Search)

- BFS는 **너비 우선 탐색** 이라고도 부르며, 그래프에서 **가까운 노드부터 우선적으로 탐색하는 알고리즘** 입니다.
- BFS는 **큐 자료구조** 를 이용하며, 구체적인 동작 과정은 다음과 같습니다.
    1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 합니다.
    2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리 합니다.
    3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복합니다.

### BFS 동작 예씨

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ae33cf5d-2458-4349-a706-e59d52160ed0/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ed928caa-5c80-4762-876b-3c87f0e207e7/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/767eae39-21c3-4358-8b15-65b3607d3be1/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d4826783-237a-44ab-8e1c-e63df03deb5a/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d9488c05-70a4-4ffb-a81c-de521d37b781/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d85207ab-649c-4f16-ad99-aabd636dbc5a/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3234ca9a-3ed2-47b5-a93a-c91ae8285853/Untitled.png)

### BFS 소스코드 예제(Python)

```python
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
	# 큐(Queue) 구현을 위해 deque 라이브러리 사용
	queue = deque([start])
	# 현재 노드를 방문 처리
	visited[start] = True
	# 큐가 빌 때까지 반복
	while queue:
		# 큐에서 하나의 원소를 뽑아 출력하기
		v = queue.popleft()
		print(v, end = " ")
		# 아직 방문하지 않은 인접한 원소들을 큐에 삽입
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
	[], // 인덱스 0에 대한 내용은 비워둠.
	[2, 3, 8],
	[1, 7],
	[1, 4, 5],
	[3, 5],
	[3, 4],
	[7],
	[2, 6, 8],
	[1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
bfs(graph, 1, visited)

# prints -> 1 2 3 8 7 4 5 6
```

### <문제> 미로 탈출: 문제 설명

- 동빈이는 N x M 크기의 직사각형 형태의 미로에 갇혔습니다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 합니다.
- 동빈이의 위치는 (1, 1)이며 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있습니다. 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있습니다. 미로는 반드시 탈출할 수 있는 형태로 제시됩니다.
- 이때 동빈이가 탈출하기 위해 움직여야하는 최소 칸의 개수를 구하세요. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산합니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/02dba8cc-eb08-4dfa-a6be-dec2aa223167/Untitled.png)

```python
from collections import deque

# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단거리 반환
    return graph[n-1][m-1]

# N, M 을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))
```
