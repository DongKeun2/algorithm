# 달리기 경주 Lv1
# 연습문제

# dct1, 이름 : 현재 등수
# dct2, 현재 등수 : 이름
# 이름이 불린 선수와 앞 선수의 값을 바꾼다.
def solution(players, callings):
    dct1 = {}
    dct2 = {}
    n = len(players)
    for i in range(n):
        dct1[players[i]] = i+1
        dct2[i+1] = players[i]
    
    for name in callings:
        now = dct1[name]
        nxt = now-1
        nxt_name = dct2[nxt]
        
        dct1[name] = nxt
        dct1[nxt_name] = now
        
        dct2[now] = nxt_name
        dct2[nxt] = name
        
    answer = []
    for i in range(1, n+1):
        answer.append(dct2[i])
    return answer