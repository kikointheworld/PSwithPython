from collections import deque, defaultdict
import sys

def input():
    return sys.stdin.readline().rstrip()


def is_bipartite_and_count_sets(graph, n):
    color = [-1] * (n + 1)  # 색상을 저장할 배열, -1로 초기화 (아직 방문하지 않은 노드)
    count = [0, 0]  # 두 집합의 크기를 저장할 리스트
    is_bipartite = True
    
    for start in range(1, n + 1):
        if color[start] == -1:  # 아직 방문하지 않은 노드에 대해 BFS 수행
            queue = deque([start])
            color[start] = 0
            count[0] += 1
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - current_color
                        count[color[neighbor]] += 1
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        is_bipartite = False
                        break
                        
                if not is_bipartite:
                    break
                    
        if not is_bipartite:
            break
    
    return is_bipartite, count

def count_initial_positions(N, edges):
    graph = defaultdict(list)
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    is_bipartite, count = is_bipartite_and_count_sets(graph, N)
    
    if not is_bipartite:
        return 0
    
    # 두 집합의 크기를 곱한 것이 초기 위치 조합의 수
    return count[0] * count[1] * 2

# 입력
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

# 결과 출력
print(count_initial_positions(N, edges))

