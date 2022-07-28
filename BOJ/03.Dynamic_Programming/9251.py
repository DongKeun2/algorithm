# LCS

import sys
input = sys.stdin.readline

n = input()
m = input()

lst = [0] * len(n)
for i in range(len(m)):
    for j in range(len(n))[::-1]:
        if max(lst[:(j+1)]) >= lst[j] and m[i] == n[j]:
            lst[j] = max(lst[:(j+1)]) + 1

print(max(lst))
