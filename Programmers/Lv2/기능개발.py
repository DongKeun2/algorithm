# 기능개발 Lv2
# 스택/큐

# 단순 구현
# 앞에서부터 개발에 필요한 기간 개발
# 계산된 기간 내에 개발이 가능한 경우 cnt ++
def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    day = 0
    cnt = 0
    for i in range(n):
        if progresses[i] + day*speeds[i] >= 100:
            cnt += 1
        else:
            if i != 0:
                answer.append(cnt)
            day = (100 - progresses[i]) // speeds[i] + 1 if (100 - progresses[i]) % speeds[i] else (100 - progresses[i]) // speeds[i]
            cnt = 1
    answer.append(cnt)
    return answer