from collections import deque

def solution(plans):
    answer = []
    stop_task = [] # (새 과제 이름, 남은 시간)
    for plan in plans:
        tmp = list(map(int, plan[1].split(":")))
        plan[1] = tmp[0] * 60 + tmp[1]
        plan[2] = int(plan[2])
    plans.sort(key = lambda x : x[1])    
    plans = deque(plans)
    
    
    while(True):
        now = plans.popleft()
        now_name, now_start, now_playtime = now
    
        # 뒤 과제가 없으면 그냥 진행
        if len(plans) == 0:
            answer.append(now_name)
            break
        
        now_end = now_start + now_playtime
        next_start = plans[0][1]
        
        if next_start < now_end:
            stop_task.append((now_name, now_end - next_start))
            continue
        elif next_start == now_end:
            answer.append(now_name)
            continue
        # 일단 기존 꺼 끝나고 stop task 있는지 확인해야함.
        left_time = next_start - now_end
        answer.append(now_name)
        while(stop_task):
            stop_name, stop_time = stop_task.pop()
            if stop_time < left_time:
                answer.append(stop_name)
                left_time -= stop_time
            elif stop_time == left_time:
                answer.append(stop_name)
                break
            else:
                stop_task.append((stop_name, stop_time - left_time))
                break
        

    
    # 남은 과제 
    while(stop_task):
        tmp, _ = stop_task.pop()
        answer.append(tmp)
    
    
    
    return answer


