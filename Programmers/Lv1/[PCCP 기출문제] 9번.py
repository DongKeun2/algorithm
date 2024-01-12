# [PCCP 기출문제] 9번 / 이웃한 칸

dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]

def solution(board, h, w):
    answer = 0
    n = len(board)
    m = len(board[0])
    for d in range(4):
        i, j = h + dh[d], w + dw[d]
        if 0 <= i < n and 0 <= j < m and board[i][j] == board[h][w]:
            answer += 1
    return answer