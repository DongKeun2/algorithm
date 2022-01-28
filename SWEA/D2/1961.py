# 숫자 배열 회전

T = int(input())

for i in range(1, T+1):

    N = int(input())

    n_list = []
    for _ in range(N):
        n_list.append(list(map(int, input().split())))

    list_90 = []
    for x in range(N):
        num = []
        for y in range(N):
            num.append(n_list[N - y - 1][x])
        list_90.append(num)

    list_180 = []

    for x in range(N):
        num = []
        for y in range(N):
            num.append(n_list[N - x - 1][N - y - 1])
        list_180.append(num)
    
    list_270 = []

    for x in range(N):
        num = []
        for y in range(N):
            num.append(n_list[y][N - x - 1])
        list_270.append(num)

    print(f'#{i}')
    
    for k in range(N):
        l_90 = ''.join(str(s) for s in list_90[k])
        l_180 = ''.join(str(s) for s in list_180[k])
        l_270 = ''.join(str(s) for s in list_270[k])

        print(l_90, l_180, l_270)


