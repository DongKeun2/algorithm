# [1차] 프렌즈4블록 Lv2
# 2018 KAKAO BLIND RECRUITMENT

# 사라질 수 있는 블록인지 확인한 뒤 왼쪽 위 좌표 저장 tmp
## tmp가 없다면 종료
## tmp가 있다면 해당 좌표 기준 4블록 제거
### 중복 방지로 사라졌는지 확인 후 answer ++
def solution(m, n, board):
    # 블록을 내려주는 작업
    def check():
        for j in range(n):
            cnt = 0
            for i in range(m)[::-1]:
                if not board[i][j]:
                    cnt += 1
                else:
                    board[i+cnt][j] = board[i][j]
                    if cnt:
                        board[i][j] = 0


    for i in range(m):
        board[i] = list(map(str, board[i]))

    answer = 0
    flag = True
    while flag:
        tmp = []
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    tmp.append((i, j))
        if tmp:
            for si, sj in tmp:
                for ei, ej in ((si, sj), (si+1, sj), (si, sj+1), (si+1, sj+1)):
                    if board[ei][ej]:
                        board[ei][ej] = 0
                        answer += 1
            check()
        else:
            flag = False
    return answer