# 2022 카카오 블라인드 Lv3

def solution(board, skill):
    def attack(si, sj, ei, ej, num):
        arr[si][sj] -= num
        arr[si][ej+1] += num
        arr[ei+1][sj] += num
        arr[ei+1][ej+1] -= num
    
    def heel(si, sj, ei, ej, num):
        arr[si][sj] += num
        arr[si][ej+1] -= num
        arr[ei+1][sj] -= num
        arr[ei+1][ej+1] += num
    
    n = len(board)
    m = len(board[0])
    # 새로운 배열에 누적합 기록
    arr = [[0]*(m+1) for _ in range(n+1)]
    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:
            attack(r1, c1, r2, c2, degree)
        else:
            heel(r1, c1, r2, c2, degree)
    
    # 누적합
    for i in range(1, n):
        for j in range(m):
            arr[i][j] += arr[i-1][j]
    for i in range(n):
        for j in range(1, m):
            arr[i][j] += arr[i][j-1]
    
    # 합친 후 조건에 만족하는 건물 수 반환
    answer = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] + board[i][j] > 0:
                answer += 1
    return answer