# 소수

M = int(input())
N = int(input())

list_p = []
for i in range(M, N+1):
    cnt = 0
    if i == 1:
        pass
    else:
        for k in range(2, i):
            if i % k == 0:
                cnt += 1
                break
        if cnt == 0:
            list_p.append(i)
if list_p == []:
    print(-1)
else:
    print(sum(list_p))
    print(list_p[0])
