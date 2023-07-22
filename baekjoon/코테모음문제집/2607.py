n = int(input())
target = input()
len_target = len(target)
alphabet_target = [0] * 27
for i in target:
    alphabet_target[ord(i) - ord("A")] += 1

words = [input() for _ in range(n - 1)]

ans = 0

def add_one(target, word):
    diff_count = 0
    cnt = 0
    for i in range(27):
        if target[i] != word[i]:
            diff_count += 1
            cnt += target[i] - word[i]

    if diff_count == 1 and cnt == 1:
        return 1
    else:
        return 0

def minus_one(target, word):
    diff_count = 0
    cnt = 0
    for i in range(27):
        if target[i] != word[i]:
            diff_count += 1
            cnt += word[i] - target[i]
    if diff_count == 1 and cnt == 1:
        return 1
    else:
        return 0

def same(target, word):
    for i in range(27):
        if target[i] != word[i]:
            return False
    return True

def change(target, word):
    diff_count = 0
    cnt = 0
    for i in range(27):
        if target[i] != word[i]:
            diff_count += 1
            if abs(target[i] - word[i]) == 1:
                cnt += target[i] - word[i]
            else:
                return False
    if diff_count == 2 and cnt == 0:
        return True
    else:
        return False


for word in words:
    alphabet_list = [0] * 27
    for i in word:
        alphabet_list[ord(i) - ord("A")] += 1


    len_word = len(word)
    
    if len_target - 1 == len_word: # word에서 한 문자를 더해야함.
        ans += add_one(alphabet_target, alphabet_list)
    elif len_target + 1 == len_word:
        ans += minus_one(alphabet_target, alphabet_list)
    elif len_target == len_word:
        if same(alphabet_target, alphabet_list) or change(alphabet_target, alphabet_list):
            ans += 1

print(ans)

    

