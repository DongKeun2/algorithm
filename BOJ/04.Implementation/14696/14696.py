# 딱지놀이

import sys
input = sys.stdin.readline

N = int(input())
result = []
for _ in range(N):
    ac = list(map(int, input().split()))
    bc = list(map(int, input().split()))

    acc = [0] * 4
    bcc = [0] * 4
    for i in range(1, ac[0]+1):
        acc[ac[i]-1] += 1
    
    for i in range(1, bc[0]+1):
        bcc[bc[i]-1] += 1
    
    for i in range(4)[::-1]:
        if acc[i] > bcc[i]:
            result = 'A'
            break
        elif acc[i] < bcc[i]:
            result = 'B'
            break
    else:
        result = 'D'

    print(result)