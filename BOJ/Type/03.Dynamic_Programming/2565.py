# 전깃줄
# 30616KB, 40ms

# 이어질 수 있는 곳 중 가장 긴 수열 길이 찾기
def under(n, i):
    maxCnt = 0
    for j in range(i):
        if n > arr[j][1] and maxCnt < tmp[j]:
            maxCnt = tmp[j]

    return(maxCnt)


N = int(input())

# N개의 전깃줄을 A전봇대 기준 정렬 
arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])
    arr.sort()

# 교차하지 않고 이어질 수 있는 전깃줄의 개수 기록
tmp = [0] * (N)
for i in range(N):
    n = arr[i][1]
    tmp[i] = under(n, i) + 1

# 전체 전깃줄에서 이어질 수 있는 전깃줄의 최대 수를 비교하여 제거할 전깃줄 수 계산
result = N - max(tmp)
print(result)
