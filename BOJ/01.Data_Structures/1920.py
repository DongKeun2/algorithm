# 수 찾기
# 자료 구조, 이분 탐색
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# n 탐색, 좌l 우r
def sol(n, l, r):
    # 중간지점
    m = (l+r)//2

    # 못 찾은 경우
    if l > r:
        return 0
    
    # 찾은 경우
    if lst[m] == n:
        return 1
    
    # 중간보다 큰 경우
    if n > lst[m]:
        return sol(n, m+1, r)
    
    # 작은경우
    elif n < lst[m]:
        return sol(n, l, m-1)


N = int(input())
lst = sorted(list(map(int, input().split())))

M = int(input())
tmp = list(map(int, input().split()))

for i in range(M):
    print(sol(tmp[i], 0, N-1))
