# 몬스터 사냥

t = int(input())

for i in range(1, t+1):
    D, L, N = map(int, input().split())

    td = 0
    n = 0
    while N > 0:
        td += D*(1+n*L/100)
        n += 1
        N -= 1
    
    print(f'#{i} {int(td)}')
