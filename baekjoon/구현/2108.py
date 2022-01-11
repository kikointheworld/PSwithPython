'''
https://www.acmicpc.net/problem/2108
'''
import sys
from collections import Counter
n = int(sys.stdin.readline())

list1 = []

for _ in range(n):
  list1.append(int(sys.stdin.readline()))

list1.sort()
# 1번째
print(round(sum(list1) / n))

# 2번째
print(list1[(n - 1) // 2])

# 3번째
nums = Counter(list1).most_common(2)
if len(nums) == 1:
  print(nums[0][0])
elif  nums[0][1] == nums[1][1]:
  print(nums[1][0])
else:
  print(nums[0][0])



'''
tmp = 1
banned_list =[]

for i in list1:
  if tmp < list1.count(i):
    banned_list = [i]
    tmp = list1.count(i)
  elif tmp == list1.count(i):
    if i not in banned_list:
      banned_list.append(i)

if len(banned_list) == 1:
  print(banned_list[0])
else:
  print(banned_list[1])
'''


# 4번째
print(list1[-1] - list1[0])
