# 간단한 압출 풀기

T = int(input())

T = int(input())

for i in range(1, T+1):
    N = int(input())
    print(f'#{i}')
    result =[]
    for _ in range(N):
        Ci, Ki = map(str, input().split())
        result.append(f'{Ci}'*int(Ki))
    word = ''.join(str(r) for r in result)

    cnt = len(word)//10

    results = []
    for k in range(0, cnt):
        results.append(word[k*10:(k+1)*10])
    results.append(word[cnt*10:])

    for k in range(len(results)):
        print(results[k])
