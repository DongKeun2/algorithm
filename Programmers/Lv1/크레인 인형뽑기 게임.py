# 크레인 인형뽑기 게임 Lv1
# 2019 카카오 개발자 겨울 인턴십

# 스택활용 풀이
# 위에서부터 탐색하여 인형이 있다면 스택 확인
# 가장 위의 인형과 같은 인형이면 answer += 2
# 다른 인형이면 스택에 쌓기
def solution(board, moves):
    answer = 0
    n = len(board)
    tmp = []
    for m in moves:
        for i in range(n):
            if board[i][m-1]:
                if tmp and tmp[-1] == board[i][m-1]:
                    answer += 2
                    tmp.pop()
                else:
                    tmp.append(board[i][m-1])
                board[i][m-1] = 0
                break
    return answer