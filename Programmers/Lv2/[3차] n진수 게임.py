# [3차] n진수 게임 Lv2
# 2018 KAKAO BLIND RECRUITMENT

# 0부터 1씩 더하며 sol 함수를 통해 n진법의 수를 구함
# lst에 저장한 뒤 순서에 맞는 숫자를 뽑아 반환
dct = {
    '10' : 'A',
    '11' : 'B',
    '12' : 'C',
    '13' : 'D',
    '14' : 'E',
    '15' : 'F',
}
def solution(n, t, m, p):
    def sol(x):
        tmp = []
        while True:
            if x < n:
                tmp.append(x)
                break
            tmp.append(x%n)
            x //= n
        return tmp[::-1]
    
    
    num = 0
    lst = []
    while len(lst) < t*m:
        lst += sol(num)
        num += 1

    answer = ''.join(str(num) if num < 10 else dct[str(num)] for num in lst[p-1::m])[:t]
    return answer