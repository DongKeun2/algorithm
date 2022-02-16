# [sw 문제해결 기본] 3일차 회문1

T = 10

for test_case in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(8)]
    result = 0
    for i in range(8):
        for j in range(8-N+1):
            if arr[i][j:j+N] == arr[i][j:j+N][::-1]:
                result += 1
            word = ''
            for l in range(j, j+N):
                word += arr[l][i]
            if word == word[::-1]:
                result += 1

    print(f'#{test_case} {result}')
