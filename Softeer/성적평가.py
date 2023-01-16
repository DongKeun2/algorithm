# [인증평가(5차) 기출] 성적 평가
# 3/5

import sys
input = sys.stdin.readline

N = int(input())

tot = [0] * N
for _ in range(3):
    scores = list(map(int, input().split()))

    tmp = [[] for _ in range(1001)]
    for i in range(N):
        tmp[scores[i]].append(i)
        tot[i] += scores[i]
    
    rank = 1
    result = [0] * N
    for member_list in tmp[::-1]:
        cnt = 0
        if member_list:
            for member in member_list:
                result[member] = rank
                cnt += 1
        rank += cnt

    print(' '.join(str(answer) for answer in result))

tmp = [[] for _ in range(3001)]
for i in range(N):
    tmp[tot[i]].append(i)

rank = 1
result = [0] * N
for member_list in tmp[::-1]:
    cnt = 0
    if member_list:
        for member in member_list:
            result[member] = rank
            cnt += 1
    rank += cnt

print(' '.join(str(answer) for answer in result))