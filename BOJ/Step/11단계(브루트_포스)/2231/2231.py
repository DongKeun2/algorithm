# 분해합

N = int(input())

for i in range(N):
    k = 0
    sum_n = 0
    for k in str(i):
        sum_n += int(k)
    if i + sum_n == N:
        print(i)
        break
else:
    print(0)
