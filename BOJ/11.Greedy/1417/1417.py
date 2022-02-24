# 국회의원 선거
# 구현 시뮬레이션 그리디

N = int(input())
lst = [int(input()) for _ in range(N)]

cnt = 0
while len(lst) > 1 and lst[0] <= max(lst[1:]):
    m = 0
    for i in range(1, N):
        if m < lst[i]:
            m = lst[i]
            idx = i
    lst[idx] -= 1
    lst[0] += 1
    cnt += 1

print(cnt)
