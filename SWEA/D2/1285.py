# 아름이의 돌 던지기

T = int(input())

for i in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))

    min_d = 100000
    cnt = 0

    for x in X:
        if abs(x) < min_d:
            min_d = abs(x)
            cnt =1
        elif x == min_d:
            cnt += 1
    
    print(f'#{i} {min_d} {cnt}')