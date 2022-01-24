# DFS (Depth-First Search)

- DFS는 **깊이 우선 탐색** 이라고도 부르며 그래프에서 **깊은 부분을 우선적으로 탐색하는 알고리즘** 입니다.
- DFS는 **스택 자료구조(혹은 재귀함수)를 이용**하며,  구체적인 동작 과정은 다음과 같습니다.
    1. 탐색 시작 노드를 스택에 삽입하고 방문처리 합니다.
    2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리합니다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냅니다.
    3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복합니다. 

### DFS 동작 예시

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7f187964-8c48-4e2b-87be-31888257bbfc/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c6ac3cb8-48d9-4e77-9cb5-ad543ae15fc4/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3406a4a3-c34e-4193-bccd-9775b7592324/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1fcd8d99-0ef2-4fa5-b55e-0527aae182f9/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5ec0a3f2-03bf-4919-acfb-850a3c939d13/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/406a0a00-6a23-4252-9c6c-2501d77216be/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d1e0d0ff-680d-4b29-ac2c-04668ba24424/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/975f50d5-da7a-41b5-8857-3cf0264606fe/Untitled.png)

### DFS 소스코드 예제(Python)

```python
# DFS 메서드 정의
def dfs(graph, v, visited):
	# 현재 노드를 방문 처리
	visited[v] = True
	print(v, end = " ")
	# 현재 노드와 연결된 다른 노드를 재귀적으로 방문
	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)

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
dfs(graph, 1, visited)

# prints -> 1 2 7 6 8 3 4 5
```

### <문제> 음료수 얼려 먹기: 문제 설명

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/910d989b-e231-4359-b7c1-6d9a7f167a54/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/82377956-6a18-42b3-a279-cc8be5a9b914/Untitled.png)

### 문제 해결 아이디어

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/90f30082-74a9-4562-9a26-ec96b21804b7/Untitled.png)

- DFS를 활용하는 알고리즘은 다음과 같습니다.
    1. 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 ‘0’이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문합니다.
    2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 진행하는 과정을 반복하면, **연결된 모든 지점을 방문** 할 수 있습니다ㅏ.
    3. 모든 노드에 대하여 1~2번의 과정을 반복하며, 방문하지 않은 지점의 수를 카운트합니다. 

### 답안 예시(Python)

```python
# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result) # 정답 출력
```

- 나의 답안
    
    ```python
    # <문제> 음료수 얼려 먹기
    import sys
    
    n, m = map(int,sys.stdin.readline().split())
    
    ice = []
    
    for _ in range(n):
        s = sys.stdin.readline().strip()
        tmp = []
        for k in range(m):
            tmp.append(int(s[k]))
        ice.append(tmp)
    
    ans = 0
    
    def change(i, j, ice):
        # 상
        if i - 1 >= 0:
            if ice[i - 1][j] == 0:
                ice[i - 1][j] = 1
                change(i - 1, j, ice)
        # 하
        if i + 1 < n:
            if ice[i + 1][j] == 0:
                ice[i + 1][j] = 1
                change(i + 1, j, ice)
        # 좌
        if j - 1 >= 0:
            if ice[i][j - 1] == 0:
                ice[i][j - 1] = 1
                change(i, j - 1, ice)
        # 우
        if j + 1 < m:
            if ice[i][j + 1] == 0:
                ice[i][j + 1] = 1
                change(i, j + 1, ice)
        
    
    for a in range(n):
        for b in range(m):
            if ice[a][b] == 1:
                continue
    
            ans += 1
            ice[a][b] = 1
            # 상, 하, 좌, 우 모두 0일 시 1로 수정해줌.
            change(a, b, ice)
    
    print(ans)
    ```
