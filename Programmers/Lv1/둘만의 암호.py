# 둘만의 암호 Lv1
# 연습문제 반복문

def solution(s, skip, index):
    dct = {}
    for w in skip:
        dct[w] = 1
    
    answer = ''
    for word in s:
        n = ord(word)
        cnt = 0
        while cnt < index:
            n += 1
            if n > 122:
                n = 97
            if chr(n) not in dct:
                cnt += 1
        answer += chr(n)
    return answer