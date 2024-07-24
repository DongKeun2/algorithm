# 소수 찾기

N = int(input())


n = list(map(int, input().split()))
cnt_0 = 0
for k in n:
    cnt = 0
    for j in range(1, k+1):
        if k % j == 0:
            cnt += 1
    if cnt == 2:
        cnt_0 += 1
print(cnt_0)