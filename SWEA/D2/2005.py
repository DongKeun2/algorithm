# 파스칼의 삼각형

T = int(input())

for i in range(1, T+1):
    N = int(input())
    list_p = []
    for j in range(1, N+1):
        list_p.append([0]*j)
    for k in range(N):
        for j in range(k+1):
            if j == 0 or j == k:
                list_p[k][j] = 1
            else:
                list_p[k][j] = list_p[k-1][j-1] + list_p[k-1][j]
    print(f'#{i}')
    for l in list_p:
        if l != [0]:
            print(' '.join(str(x) for x in l))

