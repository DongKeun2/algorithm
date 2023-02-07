# 연습문제 Lv2

def solution(want, number, discount):
    # 모든 품목이 0이라면 가능한 날
    def check():
        for value in dct.values():
            if value:
                return False
        return True

    
    # 딕셔너리 활용, 품목별 개수 저장
    dct = {}
    for i in range(len(want)):
        dct[want[i]] = number[i]
    
    # 첫째날 확인, 가능하면 +1
    answer = 0
    for i in range(10):
        if discount[i] in dct:
            dct[discount[i]] -= 1
    if check():
        answer += 1
        
    # 다음날부터 가능한지 확인
    for i in range(10, len(discount)):
        if discount[i] in dct:
            dct[discount[i]] -= 1
        if discount[i-10] in dct:
            dct[discount[i-10]] += 1
        
        # 가능한 날이면 +1
        if check():
            answer += 1
        
    return answer