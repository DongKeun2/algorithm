# 2개 이하로 다른 비트 Lv2
# 월간 코드 챌린지 시즌2

# 뒤에서부터 탐색, 0을 찾으면 1로 바꾼 뒤
# 그 지점부터 다시 앞에서부터 가장 먼저 찾은 1을 0으로 바꾼다.
def solution(numbers):
    answer = []
    for n in numbers:
        s = bin(n)[2:]
        for i in range(len(s))[::-1]:
            if s[i] == '0':
                s = s[:i] + '1' + s[i+1:]
                for j in range(i+1, len(s)):
                    if s[j] == '1':
                        s = s[:j] + '0' + s[j+1:]
                        break
                break
        else:
            s = '10' + s[1:]
        answer.append(int(s, 2))
    return answer