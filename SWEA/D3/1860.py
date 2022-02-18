# 진기의 최고급 붕어빵

T = int(input())

for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))

    result = 'Possible'
    t = 1
    tot = 0
    while N > 0:
        cnt = 0
        for l in lst:
            if M*(t-1) <= l < M*t:
                cnt += 1
        
        if cnt > tot:
            result = 'Impossible'
        
        N -= cnt
        tot += K-cnt
        t += 1

    print(f'#{test_case} {result}')