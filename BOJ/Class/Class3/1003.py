# 피보나치 함수 / 실버3

T = int(input())

cnt = [[0, 0] for _ in range(41)]
cnt[0] = [1, 0]
cnt[1] = [0, 1]
for i in range(2, 41):
    cnt[i][0] = cnt[i-1][1]
    cnt[i][1] = cnt[i-1][1] + cnt[i-2][1]
    
for _ in range(T):
    n = int(input())
    print(*cnt[n])
