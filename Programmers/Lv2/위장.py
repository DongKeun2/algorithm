# 위장 Lv2
# 해시

def solution(clothes):
    dct = {}
    for a, b in clothes:
        if b in dct:
            dct[b].append(a)
        else:
            dct[b] = [a]
    
    # 모든 경우의 수에서 아무것도 입지 않은 경우 한 가지 제외
    answer = 1
    for v in dct.values():
        answer *= (len(v)+1)
    answer -= 1
    return answer