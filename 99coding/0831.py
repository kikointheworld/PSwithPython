def solution(money):
    l = len(money)
    # 1은 무조건 1 골랐을 때, 안골랐을 때로 해야할듯
    dp1 = [[0, 0] for _ in range(l)]
    dp0 = [[0, 0] for _ in range(l)]
    
    # 0은 이 집 안털었을 때, 1은 이 집 털었을 떄
    dp1[0][1] = money[0]
    dp1[1][0], dp1[1][1] = money[0], 0
    
        
    # 0은 이 집 안털었을 때, 1은 이 집 털었을 떄
    dp0[1][0], dp0[1][1] = 0, money[1]
    
    for i in range(2, l):
        dp1[i][0] = max(dp1[i - 1][0], dp1[i - 1][1])
        dp1[i][1] = max(dp1[i - 1][0] + money[i], dp1[i - 1][1])
        dp0[i][0] = max(dp0[i - 1][0], dp0[i - 1][1])
        dp0[i][1] = max(dp0[i - 1][0] + money[i], dp0[i - 1][1])
    
    if dp1[-1][0] > max(dp0[-1]):
        return dp1[-1][0]
    else:
        return max(dp0[-1])

