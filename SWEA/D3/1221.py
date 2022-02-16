# [sw 문제해결 기본] 5일차 - GNS

## 딕셔너리로 푼 코드

# T = int(input())
#
# ndict = dict(ZRO=0, ONE=1, TWO=2, THR=3, FOR=4, FIV=5, SIX=6, SVN=7, EGT=8, NIN=9)
# cdict = {n:c for c,n in ndict.items()}
#
# for _ in range(T):
#     test_case, N = input().split()
#     lst = list(map(str, input().split()))
#     N = int(N)
#
#     result = [ndict[c] for c in lst]
#
#     for i in range(N-1):
#         mn = result[i]
#         idx = i
#         for j in range(i+1, N):
#             if mn > result[j]:
#                 mn = result[j]
#                 idx = j
#         result[i], result[idx] = result[idx], result[i]
#
#     result = [cdict[n] for n in result]
#
#     print(test_case)
#     print(*result)


T = int(input())

nlst = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for _ in range(1, T+1):
    test_case, N = input().split()
    lst = list(map(str, input().split()))

    result = []

    for num in nlst:
        for word in lst:
            if num == word:
                result.append(num)

    print(test_case)
    print(*result)
