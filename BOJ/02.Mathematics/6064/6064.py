# 카잉 달력
# 수학, 정수론, 중국인의 나머지 정리

# pypy

T =  int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())

    sa = set()
    sb = set()
    for i in range(N):
        sa.add(M*i+x)
    for i in range(M):
        sb.add(N*i+y)
    
    if sa & sb:
        sol = min(sa&sb)
    else:
        sol = -1
    
    print(sol)