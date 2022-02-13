# 가장 긴 증가하는 부분 수열 4


# 가장 긴 증가하는 부분 수열을 먼저 풀어줌
n = int(input())
a = list(map(int, input().split()))

nl = [0] * (n)
nl[0] = 1

for i in range(1, n):
    mn = 0
    for j in range(0, i):
        if a[i] > a[j]:
            if mn < nl[j]:
                mn = nl[j]
    
    nl[i] += mn + 1
## 여기까지가 가장 긴 증가하는 부분 수열


# 범위 설정을 위한 max index 찾아주기, 결과리스트 ml에 가장 큰 값 미리 넣어줌
mi = nl.index(max(nl))
ml = [a[mi]]


# 만약 max(nl) = 4라면 1개 넣어주고 3개를 찾아서 결과에 넣어줘야 함.
# 따라서 max(nl) - 1만큼 돌림 
for _ in range(max(nl) -1):
    idx = 0

    # mi 보다 작은 인덱스 범위에서 a리스트를 순회
    # a[mi]보다 작은 값들 중 nl[i]가 가장 큰 값을 찾아서 리스트에 담아줌
    for i in range(0, mi):
        if a[mi] > a[i]: 
            if idx <= nl[i]:
                idx = nl[i]
                cnt = i
    
    mi = cnt
    ml.append(a[mi])

# 거꾸로 담았으니 정렬시킨 후 출력
ml.sort()

print(max(nl))
print(*ml)