# [sw 문제해결 응용] 7일차 - 행렬찾기

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    lst = []
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[i][j] != 0:
                cnt += 1
                if (j+1) == n:
                    lst.append(cnt)
            else:
                if cnt != 0:
                    lst.append(cnt)
                    cnt = 0
    
    result = []
    for i in range(1, n+1):
        cnt = 0
        for j in range(len(lst)):
            if lst[j] == i:
                cnt += 1
        if cnt != 0:
            result.append([cnt, i])
    cnt = len(result)

    sol = []
    for i in range(len(result)-1):
        idx = i
        for j in range(i, len(result)):
            if result[idx][0]*result[idx][1] > result[j][0]*result[j][1]:
                idx = j
            elif result[idx][0]*result[idx][1] == result[j][0]*result[j][1]:
                if result[idx][0] > result[j][0]:
                    idx = j
        if idx != i:
            result[i], result[idx] = result[idx], result[i]               
        sol.append(result[i][0])
        sol.append(result[i][1])

    sol.append(result[-1][0])
    sol.append(result[-1][1])
    print(f'#{test_case} {cnt}', *sol)
