# 2023 카카오 블라인드
# Lv3

tmp = [2**(i+1) -1 for i in range(100)]

def to_binary(num):
    if num == 0 or num == 1:
        return str(num)
    return to_binary(num//2) + str(num%2)

def len_check(len_binary):
    for i in range(len(tmp)):
        if len_binary <= tmp[i]:
            return tmp[i] - len_binary
        
def sol(tmp):
    global result
    
    if len(tmp) == 1:
        return
    
    if not result:
        return
    
    middle = len(tmp)//2
    left = tmp[:middle]
    right = tmp[middle+1:]
    if tmp[middle] == '1':
        sol(left)
        sol(right)
    else:
        if max(sum(int(l) for l in left), sum(int(r) for r in right)):
            result = 0
            return

def solution(numbers):
    global result
    
    answer = []
    for number in numbers:
        binary = to_binary(number)
        binary = '0'*len_check(len(binary)) + binary
        
        result = 1
        sol(binary)

        if result:
            answer.append(1)
        else:
            answer.append(0)
    
    return answer