# 파리 퇴치

T = int(input())

for x in range(1, T+1):
    N, M = list(map(int, input().split()))

    list_N = []
    for _ in range(N):
        X = list(map(int, input().split()))
        list_N.append(X)

    max_n = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_n = 0
            for k in range(M):
                for l in range(M):
                    sum_n += list_N[i+k][j+l]
            if sum_n > max_n:
                max_n = sum_n
                
    print(f'#{x} {max_n}')
        