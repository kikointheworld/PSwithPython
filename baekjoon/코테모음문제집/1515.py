numbers = input()
len_numbers = len(numbers)
n = 1
i = 0

while(i < len_numbers):
    now_num = numbers[i]
    while(True):
        str_n = str(n)
        len_n = len(str_n)

        if now_num in str_n:
            tmp = 1
            while(True):
                if i+ tmp + 1 <= len_numbers and numbers[i:i + tmp + 1] in str_n:
                    tmp += 1
                else:
                    break
            i += tmp - 1
            n += 1
            break
        else:
            n += 1
    i += 1

print(n - 1)
