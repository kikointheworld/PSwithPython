'''
https://www.acmicpc.net/problem/2947
'''
def print_f (piece):
  for i in piece:
    print(i, end=" ")
  print()


piece = list(map(int, input().split()))
while(piece != [1, 2, 3, 4, 5]):
  for i in range(1, 5):
    if piece[i - 1] > piece[i]:
      tmp = piece[i - 1]
      piece[i - 1] =piece[i]
      piece[i] = tmp
      print_f(piece)
