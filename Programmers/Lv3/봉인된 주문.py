# 2025 프로그래머스 코드챌린지 2차 예선 lv3

# 26진수 풀이

# 수 => 문자 변환 함수
def get_num_from_str(word):
    result = 0
    for i in range(len(word)): result += (ord(word[len(word) - i - 1]) - 96) * (26**i)
    return result

# 문자 => 수 변환 함수
def get_str_from_num(num):
    result = ''
    while num >= 26:
        if num % 26:
            result = chr(num % 26 + 96) + result
            num = num // 26
        else:
            result = 'z' + result
            num = num // 26 - 1
    if num: result = chr(num % 26 + 96) + result
    return result

def solution(n, bans):
    lst = []
    for ban in bans: lst.append(get_num_from_str(ban))
    lst.sort()    
    cnt = n
    for t in lst:
        if t <= cnt: cnt += 1
    answer = get_str_from_num(cnt)
    return answer