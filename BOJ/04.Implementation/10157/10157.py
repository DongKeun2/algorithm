# 자리배정

C, R = map(int, input().split())
K = int(input())

if C*R < K:
    print(0)

else:
    arr = []
    for _ in range(R):
        arr.append([0]*C)
    
    cngx = [0, 1, 0, -1]
    cngy = [1, 0, -1, 0]
    idx = 0
    cnt = K -1
    x, y = 0, 0

    while cnt > 0:
        arr[y][x] = 1
        y += cngy[idx]
        x += cngx[idx]
        n, m = x, y
        if (y >= R) or (x >= C) or (y < 0) or (x < 0):
            y -= cngy[idx]
            x -= cngx[idx]
            idx += 1
            if idx > 3:
                idx %= 4
            y += cngy[idx]
            x += cngx[idx]
        if arr[y][x] == 1:
            y -= cngy[idx]
            x -= cngx[idx]
            idx += 1
            if idx > 3:
                idx %= 4
            y += cngy[idx]
            x += cngx[idx]
        cnt -= 1

    print(x + 1, y + 1)