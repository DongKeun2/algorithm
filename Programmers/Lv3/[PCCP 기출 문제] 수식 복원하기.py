# [PCCP 기출문제] 4번 / 수식 복원하기, LV3

# 10진수로 변환하는 함수
def radix_to_ten(word, radix):
    result = 0
    for i, n in enumerate(word[::-1]): result += int(n) * (radix ** i)
    return result

# 10진수를 radix 진수로 변환하는 함수
def ten_to_radix(n, radix):
    if not n: return '0'
    result = ''
    while n > 0:
        result = str(n % radix) + result
        n //= radix
    return result

# radix진법으로 성립하는 식인지 확인하는 함수
def is_possible_cal(a, b, c, type, radix):
    ra = radix_to_ten(a, radix)
    rb = radix_to_ten(b, radix)
    rc = radix_to_ten(c, radix)
    if type == '+' and ra + rb == rc: return True
    elif type == '-' and ra - rb == rc: return True
    return False


# 마지막 계산, 값을 특정할 수 없다면 ? 반환하는 함수
def cal_c(a, b, type, radix_lst):
    result_set = set()
    for radix in radix_lst:
        ra = radix_to_ten(a, radix)
        rb = radix_to_ten(b, radix)
        if type == '+':result_set.add(ten_to_radix(ra + rb, radix))
        else: result_set.add(ten_to_radix(ra - rb, radix))
    if len(result_set) == 1: return result_set.pop()
    return '?'

def solution(expressions):
    # a, b, c로 분류
    arr = []
    x_arr = []
    p_raidx = [1] * 10
    max_n = 1
    for ex in expressions:
        type = '+'
        if '+' in ex: tmp = ex.split('+')
        else:
            tmp = ex.split('-')
            type = '-'
        tmp1 = tmp[1].split('=')
        a = tmp[0].strip()
        b = tmp1[0].strip()
        c = tmp1[1].strip()
        for x in a+b: max_n = max(max_n, int(x))
        if c == 'X': x_arr.append((a, b, type))
        else:
            for x in c: max_n = max(max_n,int(x)) 
            arr.append((a, b, c, type))

    # 각 진법에 따라 계산이 맞는 지 확인
    for i in range(max_n+1): p_raidx[i] = 0
    for lst in arr:
        a, b, c, type = lst
        for idx in range(2, 10):
            if p_raidx[idx] and not is_possible_cal(a, b, c, type, idx):
                p_raidx[idx] = 0

    radix_lst = []
    for i in range(2, 10):
        if p_raidx[i]: radix_lst.append(i)

    # 남은 진법으로 answer 구하기
    answer = []
    for a, b, type in x_arr:
        answer.append('{} {} {} = {}'.format(a, type, b, cal_c(a, b, type, radix_lst)))
    return answer