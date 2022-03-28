# 이진수 표현

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    result = 'OFF'
    if 2**N-1 <= M:
        num = ''
        while M:
            num = str(M%2) + num
            M //= 2
        if num[len(num)-N:].count('1') == N:
            result = 'ON'

    print(f'#{test_case} {result}')
