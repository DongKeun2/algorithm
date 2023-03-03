# 혼자서 하는 틱택토 Lv2
# 연습문제

def solution(board):
    # board에 존재하는 O, X의 수
    ocnt = 0
    xcnt = 0
    # O,X의 성공 여부
    oc = 0
    xc = 0
    
    # \와 / 모양 O, X의 개수, 3개일 경우 성공여부 체크
    ox = 0
    xx = 0
    oy = 0
    xy = 0
    for i in range(3):
        # ㅡ,ㅣ 모양 O, X의 개수, 3개일 경우 성공여부 체크
        oi = 0
        oj = 0
        xi = 0
        xj = 0
        for j in range(3):
            if i == j:
                if board[i][j] == 'O':
                    ox += 1
                elif board[i][j] == 'X':
                    xx += 1
            if i+j == 2:
                if board[i][j] == 'O':
                    oy += 1
                elif board[i][j] == 'X':
                    xy += 1
                    
            if board[i][j] == 'O':
                oi += 1
            if board[j][i] == 'O':
                oj += 1
            if board[i][j] == 'X':
                xi += 1
            if board[j][i] == 'X':
                xj += 1 

        if oi >= 3 or oj >= 3:
            oc = 1
        if xi >= 3 or xj >= 3:
            xc = 1
        ocnt += board[i].count('O')
        xcnt += board[i].count('X')

    if ox >= 3 or oy >= 3:
        oc = 1
    if xx >= 3 or xy >= 3:
        xc = 1
    
    # O와 X의 개수는 같거나 O가 하나 많아야 한다.
    # O와 X는 같이 성공할 수 없다.
    # O가 승리한 경우 O가 하나 많아야 한다.
    # X가 승리한 경우 수가 같아야 한다.
    answer = 1
    if (ocnt != xcnt + 1 and ocnt != xcnt):
        answer = 0
    if oc and xc:
        answer = 0
    if oc and ocnt == xcnt:
        answer = 0
    if xc and ocnt == xcnt + 1:
        answer = 0
        
    return answer