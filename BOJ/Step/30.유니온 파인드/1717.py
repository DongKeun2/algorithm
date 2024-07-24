# 집합의 표현
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def check(c):
    # 루트 노드 찾기
    if c == lst[c]:
        return c
    p = check(lst[c])

    # 루트 노드 반환
    lst[c] = p
    return lst[c] 


def link(a, b):
    x = check(a)
    y = check(b)

    if x == y:
        return
    
    lst[x] = y


n, m = map(int, input().split())
lst = [x for x in range(n+1)]

for _ in range(m):
    s, a, b = map(int, input().split())

    # 루트 노드 연결
    if s == 0:
        link(a, b)

    # 루트 노드 일치 확인
    else:
        result = 'NO'
        if check(a) == check(b):
            result = 'YES'

        print(result)