# 달팽이 숫자

T = int(input())

for i in range(1, T+1):
    N = int(input())
    
    num_list = []
    for _ in range(N):
        num_list.append([0]*N)

    d1 = [1, 0, -1, 0]
    d2 = [0, 1, 0, -1]
    x, y = 0, 0
    c = 0
    cnt = 1

    while cnt < N**2+1:
        num_list[y][x] = cnt
        x += d1[c]
        y += d2[c]
        if x >= N or y >= N or num_list[y][x] != 0:
            x -= d1[c]
            y -= d2[c]
            c = c+1
            if c >= 4:
                c -= 4
            x += d1[c]
            y += d2[c]
        cnt += 1

    print(f'#{i}')
    for n_list in num_list:
        print(*n_list)