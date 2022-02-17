# 의석이의 세로로 말해요

T = int(input())

for test_case in range(1, T+1):
    arr = [list(input()) for _ in range(5)]

    ml = 0
    for i in range(5):
        if ml < len(arr[i]):
            ml = len(arr[i])


    result = ''
    for i in range(ml):
        for j in range(5):
            if i < len(arr[j]):
                result += arr[j][i]

    print(f'#{test_case} {result}')