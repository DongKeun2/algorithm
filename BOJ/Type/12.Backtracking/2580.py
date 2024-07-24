# 스도쿠
# 백트래킹
# pypy통과

# si, sj 위치에 n이 들어갈 수 있는 지 확인
def check(si, sj, n):
    # 가로 세로에 n이 있다면 불가능
    for k in range(9):
        if arr[si][k] == n or arr[k][sj] == n:
            return 0

    # 해당 위치의 3x3자리에 n이 있다면 불가능
    ei, ej = 3*(si//3), 3*(sj//3)
    for i in range(ei, ei+3):
        for j in range(ej, ej+3):
            if arr[i][j] == n:
                return 0
    # 없다면 가능
    return 1


def sol(idx):
    global result

    if result:
        return

    # 모든 0을 바꿔 스도쿠 완성
    if idx >= len(pos):
        result = arr
        return

    i, j = pos[idx]
    for n in range(1, 10):
        if check(i, j, n):
            arr[i][j] = n
            sol(idx+1)
            if result:
                return
            arr[i][j] = 0


arr = [list(map(int, input().split())) for _ in range(9)]

# 0이 저장된 위치 기록
pos = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            pos.append((i,j))

result = 0
sol(0)

for i in range(9):
    print(*result[i])
