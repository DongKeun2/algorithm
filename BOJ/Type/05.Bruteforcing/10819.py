# 차이를 최대로
# 브루트포스, 백트래킹

def sol():
    global result
    if len(st) == N:
        tot = 0
        for i in range(N-1):
            tot += abs(st[i] - st[i+1])
        if result < tot:
            result = tot 
            return result
        return
    else:
        for i in range(N):
            if v[i] == 0:
                v[i] = 1
                st.append(A[i])
                sol()
                st.pop()
                v[i] = 0
        return

N = int(input())
A = list(map(int, input().split()))
v = [0] * N
st = []
result = 0
sol()
print(result)
