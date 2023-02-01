# 연습문제 LV2

def solution(topping):
    n = len(topping)
    
    # 앞 뒤로 중복확인하여 저장
    one = [0] * (n + 1)
    two = [0] * (n + 1)
    set_x = set()
    set_y = set()
    x, y = 0, 0
    for i in range(n):
        if topping[i] not in set_x:
            set_x.add(topping[i])
            x += 1
        one[i+1] = x
        
        if topping[n-i-1] not in set_y:
            set_y.add(topping[n-i-1])
            y += 1
        two[n-i-1] = y

    # 같은 종류를 가질 수 있는 위치의 수 구하기
    answer = 0
    for j in range(n+1):
        if one[j] == two[j]:
            answer += 1
            
    return answer