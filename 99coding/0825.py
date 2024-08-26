from collections import deque
import math

def rotate(coords): #회전해서 최대한 0,0 에 가깝게 맞춘다
    degrees = [90,180,270,0]
    rotated_shapes = []
    keys = []# 몇번 도형인지 - 중복방지

    for idx, shapes in enumerate(coords): #모양 하나하나
        for degree in degrees: 
            rad = degree * (math.pi / 180.0)
            new_coords = []
            min_x = 50
            min_y = 50
            for coord in shapes:# 하나의 모양에 좌표가 여러개임
                x, y = coord
                nx = round(math.cos(rad)*x - math.sin(rad)*y)
                ny = round(math.sin(rad)*x + math.cos(rad)*y)
                new_coords.append([nx, ny])
                min_x =  min(min_x, nx)
                min_y =  min(min_y, ny)
            new_coords = [[sublist[0] - min_x, sublist[1] - min_y] for sublist in new_coords]
            rotated_shapes.append(sorted(new_coords))
            keys.append(idx)
    return rotated_shapes, keys


def get_shapes(q, num, board): # table일때는 1이 도형 아닐때는 0 이 도형
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    #shapes = []
    empty_board = []
    while q:
        x, y = q.popleft()
        if board[x][y] == num:
            empty_board.append([x,y])
            # 0 -> 1, 1 -> 0 으로 바꿔줘야함
            if num == 1:
                board[x][y] = 0
            else:
                board[x][y] = 1
                    
            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<len(board) and 0<=ny<len(board[0]) and board[nx][ny] == num:
                    q.append([nx, ny])
    return empty_board


def solution(game_board, table):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque()
    shapes = []
    cnt = 0
    # 테이블 도형 리스트 미리 뽑아놓기
    coloured_shapes = []
    for x in range(len(table)):
        for y in range(len(table[0])):
            q.append([x,y])
            shapes = get_shapes(q, 1, table)
            if shapes:
                coloured_shapes.append(shapes)
    rotated_shapes, keys = rotate(coloured_shapes)

    # #빈칸찾아서 도형 있는지 보기 
    for x in range(len(game_board)):
        for y in range(len(game_board[0])):
            q.append([x,y])
            shapes = get_shapes(q, 0, game_board)
            # 빈칸모양도 0,0 기준으로 바꾸자
            if shapes:
                min_x= min(sublist[0] for sublist in shapes)
                min_y = min(sublist[1] for sublist in shapes)
                shapes = [[sublist[0] - min_x, sublist[1] - min_y] for sublist in shapes]
            
                if sorted(shapes) in rotated_shapes:
                    shapes_idx = rotated_shapes.index(sorted(shapes))
                    val = shapes_idx // 4
                    del rotated_shapes[val*4:(val*4)+4]
                    cnt += len(shapes)

    return cnt
