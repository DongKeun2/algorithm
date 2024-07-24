# 가르침
# 브루트포스, 비트마스킹, 백트래킹

from itertools import combinations

# 만약 lst에 있는 알파벳을 배웠다면 몇 개의 단어를 읽을까?
def sol(lst):
    global result
    
    cnt = 0
    for word in words:
        if word & lst == word:
            cnt += 1

    if result < cnt:
        result = cnt


# 단어의 수, 배울 수 있는 알파벳 수
N, K = map(int, input().split())

# 단어마다 배워야 할 알파벳
words = [set(input())-{'a','n','t','i','c'} for _ in range(N)]

# 배워야 할 전체 알파벳
alp = set()
for word in words:
    for s in word:
        alp.add(s)

# 모든 알파벳을 배울 수 있다면 N개의 단어를 읽을 수 있다.
if len(alp) > K-5:
    result = 0
    # 5개 미만이라면 어떤 단어도 배울 수 없다.
    if K >= 5:
        arr = list(combinations(alp, K-5))
    else:
        print(result)
        exit()
        
    for i in range(len(arr)):
        sol(set(arr[i]))
else:
    result = N

print(result)
