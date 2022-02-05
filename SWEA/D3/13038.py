
def day_cal(a):
    day_l = []
    for idx in il:
        if idx ==0:
            nl = a[idx::]
        else:
            nl = a[idx:] + a[:idx]
        day_c = 0
        nn = int(n)
        while nn != 0:
            for x in nl:
                if x == 1:
                    nn -= 1
                    day_c += 1
                    if nn == 0:
                        break
                else:
                    day_c += 1
        day_l.append(day_c)
    return day_l

tc = int(input())

for i in range(1, tc+1):
    n = int(input())
    a = list(map(int, input().split()))

    il = [idx for idx, x in enumerate(a) if x == 1]

    day = min(day_cal(a))
    print(f'#{i} {day}')
