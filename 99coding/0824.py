from collections import deque

def solution(tickets):
    answer = []
    # 출발지, 목적지 기준 정렬
    # 출발지를 기준으로 정렬하면 출발지가 같은 것끼리 인접하도록 정렬되고,
    # 특정 공항이 출발지인 티켓을 쉽게 연속적으로 순회 가능함
    # 목적지를 기준으로 정렬하면 알파벳 순서 상 앞선 도착지를 먼저 방문할 수 있으므로,
    # 최초의 완성 루트를 발견하면 그게 곧 알파벳 순서 상 가장 앞선 완성 루트가 됨
    tickets.sort(key = lambda x: (x[0], x[1]))
    
    # 현재까지의 경로와, 남은 티켓을 큐에 튜플로 저장
    dq = deque([(["ICN"], tickets)])
    
    while dq:
        now_path, now_t = dq.popleft()
        
        # 남은 티켓이 없다면, 그 때의 path가 알파벳 순서 상 가장 앞선 완성된 루트임
        if len(now_t) == 0:
            answer = now_path
            break
        
        # 출발지가 현재 위치한 공항과 같은 티켓 중 가장 왼쪽 거에서 idx를 멈춤
        valid_idx = -1
        for i in range(len(now_t)):
            if now_t[i][0] == now_path[-1]:
                valid_idx = i
                break
        
        # 남은 티켓이 있는 상태에서 다른 공항으로 가는 티켓도 없으므로 현재 루트는
        # 유효하지 않은 루트이므로 continue
        if valid_idx == -1:
            continue
        
        # 출발지가 현재 위치한 공항인 티켓을 차례로 순회하며 정보를 큐에 넣어줌
        while valid_idx < len(now_t) and now_t[valid_idx][0] == now_path[-1]:
            dq.append((now_path + [now_t[valid_idx][1]], now_t[:valid_idx] + now_t[valid_idx+1:]))
            
            valid_idx += 1
        
    return answer
