# 2019 카카오 개발자 겨울 인턴십 Lv2

def solution(s):
    lst = list(x.lstrip('{').rstrip('}') for x in s.split(','))
    
    # s에 각 숫자가 몇 번 등장하는지 계산
    dct = {}
    for n in lst:
        if n in dct:
            dct[n] += 1
        else:
            dct[n] = 1
    
    # 가장 많이 등장하는 수부터 리스트에 담기
    tmp = {v:int(k) for k, v in dct.items()}
    answer = []
    idx = int(max(dct.values()))
    while idx > 0:
        answer.append(tmp[idx])
        idx -= 1
    
    return answer