# 동전 0

def sol(K):
    total = K
    cnt = 0
    for i in range(N):
        cnt += total//lst[i]
        total = total%lst[i]
    return cnt


N, K = map(int, input().split())

lst = [int(input()) for _ in range(N)]
lst.reverse()

result = sol(K)

print(result)