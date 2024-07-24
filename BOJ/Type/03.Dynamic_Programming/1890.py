# 점프
# 30616KB, 40ms

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

tmp = [[0]*N for _ in range(N)]
tmp[0][arr[0][0]], tmp[arr[0][0]][0] = 1, 1

for i in range(N):
    for j in range(N):
        if tmp[i][j] != 0 and arr[i][j] != 0:
            ei, ej = i+arr[i][j], j+arr[i][j]
            if ei < N:
                tmp[ei][j] += tmp[i][j]
            if ej < N:
                tmp[i][ej] += tmp[i][j]

print(tmp[N-1][N-1])

## 시간초과
# def sol(si, sj):
#     global result
#     jump = arr[si][sj]

#     ei, ej = si + jump, sj + jump

#     if (si == N-1 and ej == N-1) or (ei == N-1 and sj == N-1):
#         result += 1
#         return
    
#     if ei < N:
#         sol(ei, sj)
    
#     if ej < N:
#         sol(si, ej)



# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]

# result = 0
# sol(0, 0)

# print(result)