import sys

n, GAME_TYPE = map(str, sys.stdin.readline().split())
n = int(n)

player_list = set([])

for _ in range(n):
    player_list.add(sys.stdin.readline().rstrip())

min_players = 1

if GAME_TYPE == 'F':
    min_players = 2
elif GAME_TYPE == "O":
    min_players = 3

print(len(player_list) // min_players)
