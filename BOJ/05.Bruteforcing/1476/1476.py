# 날짜 계산

years = list(map(int, input().split()))

y = 1
lst = [1, 1, 1]

while lst != years:
    y += 1
    lst[0] = lst[0]%15 + 1
    lst[1] = lst[1]%28 + 1
    lst[2] = lst[2]%19 + 1

print(y)