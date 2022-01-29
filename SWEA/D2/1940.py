# 가랏! RC카!

T = int(input())

for i in range(1, T+1):
    n = int(input())

    v = 0
    d = 0
    for _ in range(n):
        c = list(map(int, input().split()))

        if c[0] == 1:
            v += c[1]
            d += v
        elif c[0] == 2:
            v -= c[1]
            if v < 0:
                v = 0
            d += v
        else:
            d += v
    
    print(f'#{i} {d}')