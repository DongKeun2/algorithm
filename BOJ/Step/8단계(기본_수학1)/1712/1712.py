# 손익분기점

A, B, C = list(map(int, input().split()))

if B >= C:
    print(-1)
else:
    cnt = A//(C-B) + 1
    print(cnt)