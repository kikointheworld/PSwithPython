'''
https://www.acmicpc.net/problem/1966
'''

testcase_num = int(input())

for _ in range(testcase_num):
  n, m = map(int, input().split())
  tmp_list = list(map(int, input().split()))
  index_list = list(range(0, n))
  ans = 1

  while(True):
    if tmp_list[0] == max(tmp_list):
      tmp_list.pop(0)
      if index_list[0] == m:
        print(ans)
        break
      index_list.pop(0)
      ans += 1
      
    else:
      tmp_list.append(tmp_list.pop(0))
      index_list.append(index_list.pop(0))
    
