# 24시간

T = int(input())

for i in range(1, T+1):
    a, b =  map(int, input().split())
    t = a+b
    if t >= 24:
        t -= 24
    print(f'#{i} {t}')