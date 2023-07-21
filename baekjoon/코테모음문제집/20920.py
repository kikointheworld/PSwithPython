n, m = map(int, input().split())

lists = dict()

for i in range(n):
    word = input()
    if len(word) >= m:
        if word not in lists:
            lists[word] = 1
        else:
            lists[word] += 1
    
my_list = []
for key, value in lists.items():
    my_list.append([value, len(key), key])

my_list.sort(key = lambda x : (-x[0], -x[1], x[2]))


for i in my_list:
    print(i[2])
