T = int(input())

for tc in range(T):
    n = int(input())
    numbers = list(map(int, input().split()))

    teams = [0] * 201

    for number in numbers:
        teams[number] += 1
    
    team_list = []
    team_dict = dict()
    for i in range(1, 201):
        if teams[i] == 6:
            team_list.append(i)
            team_dict[i] = [0, 0, 0]
    
    tmp_score = 0
    for number in numbers:
        if number in team_list:
            tmp_score += 1
            if team_dict[number][0] < 4:
                team_dict[number][0] += 1
                team_dict[number][1] += tmp_score
            elif team_dict[number][0] == 4:
                team_dict[number][0] += 1
                team_dict[number][2] += tmp_score
    
    ans = -1
    best_point = 1000000
    best_5_point = 1001
    for key, value in team_dict.items():
        if value[1] < best_point:
            best_point = value[1]
            ans = key
            best_5_point = value[2]
        elif value[1] == best_point and value[2] < best_5_point:
            ans = key
            best_5_point = value[2]
            
    print(ans)



