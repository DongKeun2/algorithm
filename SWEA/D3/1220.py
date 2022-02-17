# [SW 문제해결 기본] 5일차 - Magnetic

T = 10

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                if cnt == 0 or cnt == 2:
                    cnt = 1

            elif arr[j][i] == 2:
                if cnt == 1:
                    cnt = 2
                    result += 1
            else:
                if cnt == 2:
                    cnt = 0
             
    print(f'#{test_case} {result}')
    