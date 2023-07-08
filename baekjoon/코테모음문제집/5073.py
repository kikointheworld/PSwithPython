while (True):
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break

    sides = [a, b, c]
    sides.sort()

    maxi = sides[-1]
    mini = sides[0]
    midi = sides[1]

    if maxi >= midi + mini:
        print("Invalid")
        continue

    if maxi == mini:
        print("Equilateral")
        continue

    if maxi == midi or midi == mini:
        print("Isosceles")
        continue

    print("Scalene")
