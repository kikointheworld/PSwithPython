def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zero = 0
    for i in lottos:
        if i != 0:
            if i in win_nums:
                cnt += 1
        else:
            zero += 1
            
    return [min(7 - (cnt + zero), 6), min(7 - cnt, 6)]
