# 1로 만들기

x = int(input())
cnt = [ 0 for i in range(x+1) ]

for i in range(2, x+1):
    cnt[i] = cnt[i-1] + 1

    if i%2 == 0:
        cnt[i] = min(1 + cnt[i//2], cnt[i])
    if i%3 == 0:
        cnt[i] = min(1 + cnt[i//3], cnt[i])

print(cnt[x])