# JadenCase 문자열 만들기 Lv2
# 연습문제

# 문자열 하나씩 확인
# 공백을 제외한 문자를 tmp에 저장
# ' '은 그대로, 문자열은 첫 문자만 대문자 나머지 문자를 소문자로 출력
def solution(s):
    lst = []
    tmp = ''
    for w in s:
        if w == ' ':
            if tmp:
                lst.append(tmp)
            lst.append(' ')
            tmp = ''
        else:
            tmp += w
    if tmp:
        lst.append(tmp)
    
    answer = ''
    for word in lst:
        if word == ' ':
            answer += ' '
        else:
            answer += word[0].upper() + word[1:].lower() if len(word) > 1 else word[0].upper()
    return answer