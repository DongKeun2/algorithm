# 네트워크 연결

# 대표를 찾는 재귀 함수
# 거쳐가는 모든 값에 대표값 저장
def find_p(n):
    if rep[n] == n:
        return n
    else:
        rep[n] = find_p(rep[n])
        return rep[n]

# 두 대표를 합침
def union(x, y):
    rep[rep[x]] = find_p(y)


N = int(input())
M = int(input())

# 가중치를 기준으로 재정렬
arr = []
for _ in range(M):
    a, b, c = map(int, input().split())
    arr.append([c, a, b])
arr.sort()

# 대표를 저장하는 배열
rep = [i for i in range(N+1)]

# 간선의 수 cnt 가 N-1개일 때 종료
cnt = 0
result = 0
for c, a, b in arr:
    if cnt == N-1:
        break
    if find_p(a) != find_p(b):
        cnt += 1
        result += c
        union(a, b)

print(result)