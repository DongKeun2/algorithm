# 다리놓기

def factorail(n):
    if n != 1:
        return n * factorail(n-1)
    return 1


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    # 좌우가 같으면 경우의 수 1개
    if N == M:
        print(1)
    # NCM 조합의 개수
    else:
        print(int(factorail(M) / (factorail(N) * factorail(M-N))))