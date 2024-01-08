# 색종이 만들기 / 실버2

def sol(si, ei, sj, ej):
    cnt = 0
    for i in range(si, ei):
        for j in range(sj, ej):
            if arr[i][j]:
                cnt += 1
    if cnt == 0:
        result[0] += 1
    elif cnt == ((ei - si) * (ej - sj)):
        result[1] += 1
    else:
        sol(si, si + (ei - si)//2, sj, sj + (ej-sj)//2)
        sol(si, si + (ei - si)//2, sj + (ej-sj)//2, ej)
        sol(si + (ei - si)//2, ei, sj, sj + (ej-sj)//2)
        sol(si + (ei - si)//2, ei, sj + (ej - sj)//2, ej)   

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = [0, 0]
sol(0, N, 0, N)

print(result[0])
print(result[1])
