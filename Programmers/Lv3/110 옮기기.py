# 110 옮기기 Lv3
# 월간 코드 챌린지 시즌2

def solution(s):
    answer = []
    for S in s:
        n = len(S)
        W = S
        if n >= 3:
            cnt = 0
            W = ''
            # 110의 개수 세기
            for i in range(n):
                W += S[i]
                if W[-3:] == '110':
                    W = W[:-3]
                    cnt += 1
            # 0이 없으면 맨 앞에, 있으면 마지막 0뒤에 110붙이기 
            for i in range(len(W))[::-1]:
                if W[i] == '0':
                    W = W[:i+1] + '110' * cnt + W[i+1:]
                    break
            else:
                 W = '110' * cnt + W
        answer.append(W)
    return answer
