# 경비원

j, i = map(int, input().split())
N = int(input())

nl = []
for _ in range(N):
    nl.append(list(map(int, input().split())))

d, n = map(int, input().split())

result = 0
for di, ni in nl:
    if d == 1:
        if di == 1:
            result += abs(ni -n)
        elif di == 2:
            result += min((2*j + i - n - ni), (i + n + ni))
        elif di == 3:
            result += (ni + n)
        else:
            result += (j - n + ni)
    
    elif d == 2:
        if di == 1:
            result += min((i+n+ni),(2*j+i-n-ni))
        elif di == 2:
            result += abs(ni-n)
        elif di == 3:
            result += (i-ni+n)
        else:
            result += (i+j-n-ni)

    elif d == 3:
        if di == 1:
            result += (n+ni)
        elif di == 2:
            result += (i-n+ni)
        elif di == 3:
            result += abs(ni-n)
        else:
            result += min((j+ni+n),(2*i+j-ni-n))

    else:
        if di == 1:
            result += (j-ni+n)
        elif di == 2:
            result += (i+j-ni-n)
        elif di == 3:
            result += min((j+ni+n),(2*i+j-ni-n))
        else:
            result += abs(ni-n)

print(result)