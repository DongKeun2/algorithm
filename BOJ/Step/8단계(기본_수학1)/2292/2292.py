# 벌집

N = int(input())

s= 1
cnt = 1
if N == 1:
    print(cnt)

else:
    while N > s:
        s += 6 * cnt
        cnt += 1
    print(cnt)