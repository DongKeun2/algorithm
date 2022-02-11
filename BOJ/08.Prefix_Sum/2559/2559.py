# 수열

N, K = map(int, input().split())

T = list(map(int, input().split()))

st = 0
for i in range(K):
    st += T[i]

mct = st
for i in range(K, N):
    st += T[i] - T[i-K]
    if mct < st:
        mct = st
print(mct)
