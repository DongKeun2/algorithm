# 이중우선순위큐 Lv3
# 힙(Heap)

def solution(operations):
    # 이분탐색으로 삽입 위치확인
    def check(x):
        l = 0
        r = len(lst)-1
        while l < r:
            m = (r+l)//2
            if x < lst[m]:
                r = m
            else:
                l = m+1
        if x < lst[l]:
            lst.insert(l, x)
        else:
            lst.insert(l+1, x)
    
    # 이중순위 큐 lst, 오름차순 정렬
    lst = []
    for S in operations:
        t, n = S.strip().split()
        n = int(n)
        if t == 'I':
            if lst:
                check(n)
            else:
                lst.append(n)
        else:
            if lst:
                if n == 1:
                    lst.pop(-1)
                else:
                    lst.pop(0)
    answer = [0,0]
    if lst:
        answer = [lst[-1], lst[0]]
    return answer