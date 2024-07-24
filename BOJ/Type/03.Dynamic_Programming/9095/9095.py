# 1,2,3 더하기

t = int(input())

for _ in range(t):
    n = int(input())

    nl = [0] * (n+1)
    nl[0] = 1
    nl[1] = 1
    if n >= 2:
        nl[2] = 2
        for i in range(3, n+1):
            nl[i] = nl[i-1] + nl[i-2] + nl[i-3]

    print(nl[n])