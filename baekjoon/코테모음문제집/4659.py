
moem = ["a", "e", "i", "o", "u"]


def check_1(tc):
    for i in tc:
        if i in moem:
            return True
    return False


def is_moem(i):
    if i in moem:
        return True
    else:
        return False


def check_2(tc):
    if len(tc) <= 2:
        return True

    moem_flag = is_moem(tc[0])
    tmp = 1
    for i in range(1, len(tc)):

        if moem_flag == is_moem(tc[i]):
            tmp += 1
        else:
            moem_flag = is_moem(tc[i])
            tmp = 1
        if tmp >= 3:
            return False

    return True


def check_3(tc):
    if len(tc) <= 1:
        return True

    for i in range(len(tc) - 1):
        if tc[i] == tc[i + 1] and tc[i] != 'e' and tc[i] != 'o':
            return False
    return True


while (True):
    tc = input()
    if tc == "end":
        break
    if check_1(tc) and check_2(tc) and check_3(tc):
        print(f'<{tc}> is acceptable.')
    else:
        print(f'<{tc}> is not acceptable')
