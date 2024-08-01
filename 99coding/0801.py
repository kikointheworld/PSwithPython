def solution(numbers):
    answer = ''
    values = []
    l = len(numbers)
    
    for i in range(l):
        tmp = str(numbers[i])
        now_l = len(tmp)
        for j in range(4 - now_l):
            tmp += tmp[j % now_l]
            
        
        values.append((tmp, numbers[i]))
    
    values.sort(key = lambda x : -int(x[0]))
    
    for v in values:
        answer += str(v[-1])
    if int(answer) == 0:
        answer = '0'
    
    

    return answer
