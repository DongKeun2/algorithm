# 부분수열의 합
# 브루트 포스

N = int(input())
S = list(map(int, input().split()))

# S의 부분집합의 합 중 가장 큰 합만큼 리스트 생성
lst = [0] * (sum(S)+2)

# 부분집합의 합 모두 구해주기
for i in range(1<<N):
    tot = 0
    for j in range(N):
        if i & (1<<j):
            tot += S[j]
    # 부분집합의 합이 되는 수는 1로 바꿔주기
    lst[tot] = 1

# 작은수(0)부터 1로 저장되지 않은 수 찾기
for i in range(len(lst)):
    if lst[i] == 0:
        result = i
        break

print(result)
