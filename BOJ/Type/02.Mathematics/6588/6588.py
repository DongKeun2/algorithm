# 골드바흐의 추측

def pn_s(n):
    for i in range(2, len(pnl)):
        if pnl[n-i] and pnl[i]:
            return (f'{n} = {i} + {n - i}')
    
    return "Goldbach's conjecture is wrong."

pnl = [1 for i in range(1000001)]

for i in range(2, 1001):
    if pnl[i] != 0:
        for j in range(2*i, 1000001, i):
            pnl[j] = 0

while 1:
    n = int(input())
    if n == 0:
        break
    result = pn_s(n)
    print(result)
