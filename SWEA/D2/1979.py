# 어디에 단어가 들어갈 수 있을까

T = int(input())

for i in range(1, T+1):
    N, K = list(map(int, input().split()))

    list_n = []
    for j in range(N):
        list_n.append(list(map(int, input().split())))
    
    result = 0
    for j  in range(N):
        cnt = 0
        for k in range(N):
            if list_n[j][k] == 0:
                if cnt == K:
                    result += 1
                cnt = 0
            else:
                cnt += 1
        if cnt == K:
            result += 1

    for j in range(N):
        cnt = 0
        for k in range(N):
            if list_n[k][j] == 0:
                if cnt == K:
                    result += 1
                cnt =0
            else:
                cnt += 1
        if cnt == K:
            result += 1

    print(f'#{i} {result}')
