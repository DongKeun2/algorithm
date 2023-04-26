# [3차] 압축 Lv2
# 2018 KAKAO BLIND RECRUITMENT

# dct에 문자열 : 번호 등록
# A~Z까지 1~26로 등록
# 0번 인덱스부터 다음 문자열과 합친 문자가 dct에 존재한다면 idx증가
# 없다면 해당 문자열의 dct 값을 answer에 저장 후 인덱스 증가
# 다음 문자열을 27부터 순서대로 등록 
def solution(msg):
    dct = {}
    cnt = 1
    for i in range(65, 91):
        dct[chr(i)] = cnt
        cnt += 1
        
    n = len(msg)
    answer = []
    idx = 0
    while idx < n:
        word = msg[idx]
        while idx+1 < n and word + msg[idx+1] in dct:
                idx += 1
                word += msg[idx]
        answer.append(dct[word])
        if idx+1 < n:
            dct[word + msg[idx+1]] = cnt
            cnt += 1
        idx += 1
    return answer