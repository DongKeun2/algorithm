# 격자판의 숫자 이어 붙이기

def sol(si, sj, ans):
    if len(ans) >= 7:
        if ans not in result:
            result.append(ans)
        return
    else:
        for d in range(4):
            ni = si + di[d]
            nj = sj + dj[d]
            if 0 <= ni < 4 and 0 <= nj < 4:
                ans += str(arr[ni][nj])
                sol(ni, nj, ans)
                ans = ans[:-1]


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())

for test_case in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]

    result = []
    for i in range(4):
        for j in range(4):
            ans = str(arr[i][j])
            sol(i, j, ans)
    
    print(f'#{test_case} {len(result)}')