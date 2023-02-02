# [인증평가(3차) 기출] 플레이페어 암호
# 난이도 3/5
# 62개 예제 / 각 100ms 37mb

import sys
input = sys.stdin.readline

M = input().strip()
K = input().strip()

# dct에 알파벳 별 행, 열 저장
dct = {}
i, j = 0, 0
for k in K:
    if len(dct) >= 25 or i >= 5:
        break

    if k not in dct:
        dct[k] = (i, j)
        if j >= 4:
            i += 1 
        j = (j+1)%5

# 주어진 키로 dct가 덜 채워졌을 경우 꽉 채우기
while i < 5 and len(dct) < 25:
    for idx in range(65, 91):
        if chr(idx) == 'J':
            continue

        if chr(idx) not in dct:
            dct[chr(idx)] = (i, j) 
            if j >= 4:
                i += 1 
            j = (j+1)%5

# 메시지를 lst에 쌍으로 담기 
lst = []
memo = ''
for m in M:
    if memo:
        if memo == m:
            if memo == 'X':
                memo += 'Q'
            else:
                memo += 'X'
            lst.append(memo)
            memo = m
        else:
            memo += m
            lst.append(memo)
            memo = ''
    else:
        memo = m
        
if memo:
    memo += 'X'
    lst.append(memo)

# 암호화
result = ''
tmp = {v:k for k, v in dct.items()}
for x, y in lst:
    # 1번
    if dct[x][0] == dct[y][0]:
        result += tmp[(dct[x][0], (dct[x][1] + 1)%5)]
        result += tmp[(dct[y][0], (dct[y][1] + 1)%5)]
    
    # 2번
    elif dct[x][1] == dct[y][1]:
        result += tmp[((dct[x][0] + 1)%5, dct[x][1])]
        result += tmp[((dct[y][0] + 1)%5, dct[y][1])]
    
    # 3번
    else:
        result += tmp[(dct[x][0], dct[y][1])]
        result += tmp[(dct[y][0], dct[x][1])]

print(result)