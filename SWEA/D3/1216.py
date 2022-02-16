# [sw 문제해결 기본] 3일차 - 회문2

for _ in range(10):
    test_case = int(input())
    arr = [input() for _ in range(100)]
    result = 1
    for N in range(2, 101):
        if result >= 100:
            break
        for i in range(100):
            if result >= 100:
                break
            for j in range(100-N+1):
                if arr[i][j:j+N] == arr[i][j:j+N][::-1]:
                    if result < N:
                        result = N
                    if result >= 100:
                        break
                word = ''
                for l in range(j, j+N):
                    word += arr[l][i]
                if word == word[::-1]:
                    if result < N:
                        result = N
                    if result >= 100:
                        break

    print(f'#{test_case} {result}')
    