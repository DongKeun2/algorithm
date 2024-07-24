# 부분수열의 합
# 브루트포스, 백트래킹

N, S = map(int, input().split())
lst = list(map(int, input().split()))

cnt = 0
for i in range(1<<N):
    num = []
    for j in range(N):
        if i & (1<<j):
            num.append(lst[j])
    if num and sum(num) == S:
        cnt += 1

print(cnt)
