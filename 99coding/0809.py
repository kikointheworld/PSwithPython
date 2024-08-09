def solution(name):
    ans = 0
    l = len(name)
    moves = l - 1
    for i in range(l):
        ans += min(ord(name[i]) - ord("A"), ord("Z") + 1 - ord(name[i]))
        
        next = i + 1
        while(next < l and name[next] == 'A'):
            next += 1
        # next - 1 가 a 위치의 마지막일듯.
        moves = min(moves, 2 * i + l - next, i + 2 * (l - next))

            
        
    return ans + moves
