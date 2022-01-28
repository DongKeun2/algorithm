
T = int(input())

for i in range(1, T+1):
    m1, d1, m2, d2 = list(map(int, input().split()))

    y = [
        (1, 31),
        (2, 28),
        (3, 31),
        (4, 30),
        (5, 31),
        (6, 30),
        (7, 31),
        (8, 31),
        (9, 30),
        (10, 31),
        (11, 30),
        (12, 31),
    ]

    day = 1
    m = m2 - m1 

    if m == 0:
        day += d2 - d1

    elif m == 1:
        day += y[m1-1][1] - d1 + d2

    else:
        for j in range(m1, m2-1):
            day += y[j][1]
        day += y[m1-1][1] - d1 + d2

    print(f'#{i} {day}')