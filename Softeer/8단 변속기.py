# 8단 변속기 Lv2

import sys
input = sys.stdin.readline

lst = list(map(int, input().split()))
memo = lst[0]

result = 'mixed'
# 순차적 증가면 ascending
if memo == 1:
    for i in range(1, len(lst)):
        if memo < lst[i]:
            memo = lst[i]
        else:
            break
    else:
        result = 'ascending'

# 순차적 감소면 descending
elif memo == 8:
    for i in range(1, len(lst)):
        if memo > lst[i]:
            memo = lst[i]
        else:
            break
    else:
        result = 'descending'

print(result)