# 연습문제 Lv2

# 2진수 변환 함수
def sol(n):
    if n <= 1:
        return str(n)
    
    n = int(n)
    return str(sol(n//2)) + str(n%2)
        

def solution(data, col, row_begin, row_end):
    # 조건에 맞게 정렬
    data.sort(key=lambda item : (item[col-1], -item[0]))
    
    # S_i 구해서 tmp에 저장
    tmp = []
    for i in range(row_begin-1, row_end):
        S = 0
        for n in data[i]:
            S += n % (i+1)
        tmp.append(S)
    
    # S_i에 대해 10진수 => 2진수 변환
    bits = []
    for num in tmp:
        bits.append(sol(num))
    
    # XOR 연산
    answer = '0'
    for bit in bits:
        if len(answer) > len(bit):
            bit = '0' * (len(answer) - len(bit)) + bit
        else:
            answer = '0' * (len(bit) - len(answer)) + answer
        
        result = ''
        for i in range(len(bit)):
            if bit[i] == answer[i]:
                result += '0'
            else:
                result += '1'
        answer = result
    
    # 2진수 => 10진수 변환
    answer = int('0b{}'.format(answer), 2)
    return answer