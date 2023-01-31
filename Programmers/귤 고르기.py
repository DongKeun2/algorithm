# 연습문제 LV2

def solution(k, tangerine):
    # 딕셔너리에 귤 크기별 개수 저장 
    dct = {}
    for size in tangerine:
        if size in dct:
            dct[size] += 1
        else:
            dct[size] = 1
    
    # 큰 개수를 우선적으로 담았을 때 종류가 최소가 된다.
    tmp = sorted(dct.values(), reverse=True)
    for i in range(len(tmp)):
        if tmp[i] <= k:
            k -= tmp[i]
            if k <= 0:
                answer = i + 1
                break
        else:
            answer = i + 1
            break
    else:
        answer = 0
    
    return answer