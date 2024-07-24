# 에너지 모으기

def sol(lst, tot):
    global result

    # 두 개만 남았다면 종료
    if len(lst) <= 2:
        if result < tot:
            result = tot
        return

    # 처음과 마지막을 제외하고 양쪽의 곱을 더해주며 넘겨주기
    for i in range(1,len(lst)-1):
        n = lst.pop(i)
        sol(lst, tot+lst[i-1]*lst[i])
        lst.insert(i, n)
    

N = int(input())
lst = list(map(int, input().split()))

result = 0
sol(lst, 0)

print(result)