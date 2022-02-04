# 부녀회장이 될테야

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    f0 = []
    for x in range(1, n+1):
        f0.append(x)
    if n == 1:
        print(1)
    else:
        for i in range(k):
            for j in range(1, n):
                f0[j] += f0[j-1]
        print(f0[len(f0)-1])
