import sys
from collections import deque
input = sys.stdin.readline

p, m = map(int, input().rstrip().split())
room_people_q = []
room_num = []

# 방 정보 [ people num, [(l, n) pairs]]

for _ in range(p):
    l, n = map(str, input().rstrip().split())
    l = int(l)

    no_room = True
    for i in range(len(room_num)):
        if room_people_q[i][0][0] - 10 <= l <= room_people_q[i][0][0] + 10 and room_num[i] < m:
            room_num[i] += 1
            room_people_q[i].append([l, n])
            no_room = False
            break
    
    if no_room:
        room_people_q.append([[l, n]])
        room_num.append(1)


for i in range(len(room_num)):
    room_people_q[i].sort(key = lambda x : x[1])
    if room_num[i] == m:
        print("Started!")
    else:
        print("Waiting!")
    for room in room_people_q[i]:
        print(room[0], room[1])
    







