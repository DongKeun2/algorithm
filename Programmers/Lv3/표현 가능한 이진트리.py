# 2023 카카오 블라인드
# Lv3

# 포화 트리의 높이에 따른 노드 수 
tmp = [2**(i+1) -1 for i in range(100)]

# 2진수 변환 함수
def to_binary(num):
    if num == 0 or num == 1:
        return str(num)
    return to_binary(num//2) + str(num%2)

# 변환된 이진수의 길이를 포화 이진트리에 맞게 맞추기
def len_check(len_binary):
    for i in range(len(tmp)):
        if len_binary <= tmp[i]:
            return tmp[i] - len_binary

# 최상위 노드를 기준으로 좌, 우 확인
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

    # 최상위 노드가 0인데 자식 노드가 존재하면 불가능
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