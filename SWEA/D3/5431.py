# 민석이의 과제 체크하기

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    n = list(map(int, input().split()))

    s = [i for i in range(1, N+1)]

    ss = set(s)
    ns = set(n)
    result = ss-ns
    result = list(result)
    result.sort

    print(f'#{test_case}', *result)
