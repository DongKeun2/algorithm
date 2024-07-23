# 미세먼지 안녕! / 골드4

dist = [(1, 0, -1, 0), (0, 1, 0, -1)]
u_dist_idx = (2, 1, 0, 3)
d_dist_idx = (0, 1, 2, 3)


def diffusion():
    dust_lst = []
    for i in range(C):
        for j in range(R):
            if arr[i][j] and not arr[i][j] == -1:
                dust_lst.append((i, j, arr[i][j]))
                arr[i][j] = 0

    for si, sj, dust in dust_lst:
        cnt = 0
        for d in range(4):
            ei, ej = si + dist[0][d], sj + dist[1][d]
            if 0 <= ei < C and 0 <= ej < R and not arr[ei][ej] == -1:
                cnt += dust // 5
                arr[ei][ej] += dust // 5
        arr[si][sj] += dust - cnt
    return



def wind():
    si, sj = u_idx, 0
    idx = 0
    while True:
        ei, ej = si + dist[0][u_dist_idx[idx]], sj + dist[1][u_dist_idx[idx]] 
        if 0 <= ei <= u_idx and 0 <= ej < R:
            if arr[ei][ej] == -1:
                arr[si][sj] = 0
                break
            arr[si][sj] = -1 if arr[si][sj] == -1 else arr[ei][ej]
        else:
            if idx >= 3:
                break
            idx += 1
            ei, ej = si, sj
        si, sj = ei, ej
        
    si, sj = d_idx, 0
    idx = 0
    while True:
        ei, ej = si + dist[0][d_dist_idx[idx]], sj + dist[1][d_dist_idx[idx]] 
        if d_idx <= ei < C and 0 <= ej < R:
            if arr[ei][ej] == -1:
                arr[si][sj] = 0
                break
            arr[si][sj] = -1 if arr[si][sj] == -1 else arr[ei][ej]
        else:
            if idx >= 3:
                break
            idx += 1
            ei, ej = si, sj
        si, sj = ei, ej
    return


def sol():
    cnt = 2
    for i in range(C):
        cnt += sum(arr[i])
    return cnt

C, R, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(C)]


air_condition = []
for i in range(C):
    if arr[i][0] == -1:
        air_condition.append(i)
u_idx, d_idx = air_condition

for _ in range(T):
    diffusion()
    wind()
print(sol())