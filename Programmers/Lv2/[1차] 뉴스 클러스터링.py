# [1차] 뉴스 클러스터링 Lv2
# 2018 KAKAO BLIND RECRUITMENT

def solution(str1, str2):
    
    # str1에서 조건에 만족하는 문자 lst에 저장
    lst = []
    n = len(str1)
    for i in range(n-1):
        S = str1[i].lower()+str1[i+1].lower()
        if S.isalpha():
            lst.append(S)
    
    # str2에서 조건에 만족하는 문자만 확인
    # lst에 있다면 lst에서 제거한 뒤 cnt +1
    tot = 0
    cnt = 0
    m = len(str2)
    for i in range(m-1):
        S = str2[i].lower() + str2[i+1].lower()
        if S.isalpha():
            if S in lst:
                cnt += 1
                lst.pop(lst.index(S))
            tot += 1
    tot += len(lst)

    if tot:
        answer = int(cnt/tot * 65536)
    else:
        answer = 65536
    return answer