T = int(input())

for tc in range(T):
    n, k, t, m = map(int, input().split())
    score_list = [[0] * k for _ in range(n)]
    m_count = [0] * n
    time_count = [0] * n
    for time in range(m):
        i, j, s = map(int, input().split())
        i -= 1
        j -= 1
        score_list[i][j] = max(score_list[i][j], s)
        m_count[i] += 1
        time_count[i] = time
    
    ans = 1
    my_score = sum(score_list[t -1])
    my_m = m_count[t - 1]
    my_time = time_count[t - 1]
    for now_team in range(n):
        if now_team == t - 1:
            continue

        other_score = sum(score_list[now_team])
        other_m = m_count[now_team]
        other_time = time_count[now_team]

        if other_score > my_score:
            ans += 1
        elif other_score == my_score:
            if other_m < my_m:
                ans += 1
            elif other_m == my_m:
                if other_time < my_time:
                    ans += 1
    print(ans)


    

    



