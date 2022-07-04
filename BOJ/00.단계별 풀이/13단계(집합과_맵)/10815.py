# 숫자 카드
# 자료구조, 정렬, 이분탐색

def sol(num, l, r):
    tmp = lst[(l+r)//2]
    if num == tmp:
        return 1

    if l >= r:
        return 0
    
    if num > tmp:
        return sol(num, (l+r)//2 + 1, r)
    else:
        return sol(num, l, (l+r)//2 - 1)    


N = int(input())

lst = list(map(int, input().split()))
lst.sort()

M = int(input())

tg = list(map(int, input().split()))

result = []
for n in tg:
    result.append(sol(n, 0, N-1))
    
print(*result)