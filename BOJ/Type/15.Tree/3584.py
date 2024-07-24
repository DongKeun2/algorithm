# 가장 가까운 공통 조상
import sys
input = sys.stdin.readline

def sol(a, b):
    global result

    # a, b의 부모를 루트까지 순서대로 저장
    tmp_a = [a]
    tmp_b = [b]

    c = a
    while lst[c]:
        tmp_a.append(lst[c])
        c = lst[c]

    c = b
    while lst[c]:
        tmp_b.append(lst[c])
        c = lst[c]
    
    # 하나씩 꺼내보며 비교, 다른 순간이 온다면 그 부모가 정답
    while True:
        if tmp_a and tmp_b:
            n = tmp_a.pop()
            m = tmp_b.pop()
            if n != m:
                result = lst[n]
                return
        else:
            break


    if tmp_a:
        result = b
        return
    if tmp_b:
        result = a
        return


T = int(input())

for test_case in range(T):
    N = int(input())

    lst = [0 for _ in range(N+1)]
    for _ in range(N-1):
        p, c = map(int, input().split())
        lst[c] = p

    a, b = map(int, input().split())
    
    result = 0
    sol(a, b)

    print(result)