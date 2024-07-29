def solution(queue1, queue2):
    answer = -1
    
    q = queue1 + queue2
    l = len(q)
    total_sum = sum(q)

    if total_sum % 2 == 1:
        return -1
 
    left, right = len(queue1) - 1, l - 1
    one, two = sum(queue1), sum(queue2) 



    cnt = 0
    while(True):
        print(f"one: {one}, two: {two}")
        if one == two:
            answer = cnt
            break
        if cnt >= l * 2:
            break

        if one > two:
            print('right + 1')
            right = (right + 1) % l
            one -= q[right] 
            two += q[right] 

        else:
            print('left + 1')
            left = (left + 1) % l
            one += q[left] 
            two -= q[left] 

        cnt += 1

    return answer


