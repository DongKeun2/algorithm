# LCS

import sys
input = sys.stdin.readline

n = input().rstrip()
m = input().rstrip()

arr = [[0]*(len(m)+1) for _ in range(len(n)+1)]
for i in range(len(n)+1):
    for j in range(len(m)+1):
        if i == 0 or j == 0:
            arr[i][j] = 0
        elif n[i-1] == m[j-1]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])

print(arr[len(n)][len(m)])
