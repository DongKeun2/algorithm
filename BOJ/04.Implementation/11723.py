# 집합
# 구현, 비트마스킹

# sys의 중요성
import sys
input = sys.stdin.readline

M = int(input())
S = set()
for _ in range(M):
    lst = input().strip().split()
    cmd = lst[0]
    if len(lst) > 1:
        n = int(lst[1])
    if cmd == 'add':
        S.add(n)
    elif cmd == 'remove':
        if n in S:
            S.remove(n)
    elif cmd == 'check':
        if n in S:
            print(1)
        else:
            print(0)
    elif cmd == 'toggle':
        if n in S:
            S.remove(n)
        else:
            S.add(n)
    elif cmd == 'all':
        S = set([i for i in range(1, 21)])
    else:
        S = set()
