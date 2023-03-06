# [인증평가(2차) 기출] 사물인식 최소 면적 산출 프로그램 Lv3
# 754ms 47.91Mb

import sys
input = sys.stdin.readline

# dfs로 최소 면적 갱신
def sol(idx, x1, y1, x2, y2):
    global answer

    # 모든 색에 대해서 확인 후 면적 갱신
    if idx >= K:
        area = (x1 - x2) * (y1 - y2)
        answer = min(answer, area)
        return

    # x, y 각각 최솟값, 최댓값 활용 면적 계산
    for x, y in arr[idx+1]:
        xm = max(x, x1)
        ym = max(y, y1)
        xn = min(x, x2)
        yn = min(y, y2)
        area = (xm - xn) * (ym - yn)
        if area < answer:
            sol(idx+1, xm, ym,xn, yn)
    

N, K = map(int, input().split())

arr = [[] for _ in range(K+1)]
for _ in range(N):
    x, y, k = map(int, input().split())
    arr[k].append((x, y))

answer = 10 ** 18
for x,y in arr[1]:
    sol(1, x, y, x, y)

print(answer)