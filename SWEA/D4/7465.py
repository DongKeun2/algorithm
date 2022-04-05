# 청용 마을 무리의 개수
# kruskal

# 해당 노드의 대표자 정점 찾기
def find_set(n):
    while n != rep[n]:
        n = rep[n]
    return n

# 연결하는 u v 대표자 일치 시켜주기
def union(u, v):
    rep[find_set(v)] = find_set(u)


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    rep = [i for i in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        union(u, v)

    result = 0
    for i in range(1, N+1):
        if i == rep[i]:
            result += 1

    print(f'#{test_case} {result}')