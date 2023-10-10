# 대충 만든 자판 Lv1
# 연습문제

def solution(keymap, targets):
    def sol(i):
        cnt = 0
        for j in range(len(targets[i])):
            if targets[i][j] not in dct:
                return -1
            else:
                cnt += dct[targets[i][j]]
        return cnt
    
    answer = []
    n = len(keymap)
    m = len(targets)
    dct= {}
    for i in range(n):
        for j in range(len(keymap[i])):
            if keymap[i][j] not in dct:
                dct[keymap[i][j]] = j+1
            elif keymap[i][j] in dct and j+1 < dct[keymap[i][j]]:
                dct[keymap[i][j]] = j+1
    
    for i in range(m):
        answer.append(sol(i))
    return answer