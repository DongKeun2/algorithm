# 제곱수의 합
# pypy

n = int(input())

nl = [0]*(n+1)

for i in range(1, n+1):
    x =1
    rl = []
    while x**2 <= i:
        rl.append(nl[i-x**2])
        x += 1
    
    nl[i] = min(rl) + 1

print(nl[n])