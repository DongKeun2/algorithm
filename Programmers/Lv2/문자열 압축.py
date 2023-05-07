# 문자열 압축 Lv2
# 2020 KAKAO BLIND RECRUITMENT

# s의 길이 n
# 1부터 n까지의 단위로 잘라 압축
def solution(s):
    # tmp로 압축한 뒤 길이를 반환해주는 함수 check
    # bef에 이전 문자열 저장, 압축 가능한 수 cnt 계산
    # cnt가 1이라면 bef만 tmp에 붙이고
    ## cnt가 2 이상이라면 tmp에 cnt와 bef를 붙여줌
    def check(l):
        tmp = ''
        bef = s[:l]
        cnt = 1
        for j in range(l, n, l):
            if bef == s[j:j+l]:
                cnt += 1
            else:
                if cnt == 1:
                    tmp += bef
                else:
                    tmp += str(cnt) + bef
                cnt = 1
                bef = s[j:j+l]
        
        if cnt == 1:
            tmp += bef
        else:
            tmp += str(cnt) + bef
        return len(tmp)
    
    
    n = len(s)
    answer = n
    for i in range(1, n):
        answer = min(answer, check(i))
    return answer