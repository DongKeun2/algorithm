# 최대 성적표 만들기

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    for i in range(N):
        idx = i
        for j in range(i,N):
            if lst[idx] < lst[j]:
                idx = j
        
        lst[i], lst[idx] = lst[idx], lst[i]

    result = 0
    for i in range(K):
        result += lst[i]
    
    print(f'#{test_case} {result}')