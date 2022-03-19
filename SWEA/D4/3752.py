# 가능한 시험 점수

def sol():
    for i in range(N):
        for j in range(len(result)):
            if vst[lst[i]+result[j]] == 0:
                vst[lst[i]+result[j]] = 1
                result.append(lst[i] + result[j])
    return


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    vst = [0] * (sum(lst)+1)

    vst[0] = 1
    result = [0]
    sol()

    print(f'#{test_case} {len(result)}')
