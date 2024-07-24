# 행운의 바퀴
# 구현 시뮬레이션

N, K = map(int, input().split())

result = ['?' for _ in range(N)]
lst = [map(str, input().split()) for _ in range(K)]
cnt = 0
for i in range(K):
    S, a = lst[i]

    cnt += int(S)
    if result[cnt%N] == '?':
        if a in result:
            result = '!'
            break
        result[cnt%N] = a
    elif result[cnt%N] != a:
        result = '!'
        break

sol = result[cnt%N::-1] + result[:cnt%N:-1]

print(''.join(sol))
    