# 나무 자르기, 실버2

N, M = map(int, input().split())
lst = list(map(int, input().split()))

l = 0
r = max(lst)
answer = 0
while l < r:
    m = (l+r)//2
    s = 0
    for h in lst:
        s += h - m if h > m else 0
    if M <= s:
        l = m+1
        if answer <  m: answer = m
    else: r = m
print(answer)
 