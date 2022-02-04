# 소인수분해

N = int(input())

if N == 1:
    pass
else:
    X = N
    while X != 1:
        for k in range(2, N+1):
            if X % k == 0:
                X = X//k
                print(k)
                break
