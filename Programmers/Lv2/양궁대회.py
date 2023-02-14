# 2022 카카오 블라인드 Lv2

def solution(n, info):
    global answer, tmp
    # 적은 점수를 더 많이 획득한 경우를 위해 못 얻은 경우를 먼저 재귀
    def sol(idx, cnt, score, target, arr):
        global answer, tmp, answer_min
        # 더 많이 쏘면 종료
        if cnt > n:
            return
        
        # 1~10점 확인 후 종료 / 라이언의 점수가 더 높다면 갱신
        # 남은 화살은 0점에 기록
        if idx >= 10:
            if score > target:
                arr += [n-cnt]
                if tmp < score - target:
                    tmp = score - target
                    answer = arr
                # 가장 적은 점수를 더 많이 맞힌 경우 계산
                if tmp == score - target:
                    for i in range(10, -1, -1):
                        if answer[i] > arr[i]:
                            return
                        elif answer[i] < arr[i]:
                            answer = arr
                            return
            return
        
        num = 10 - idx
        t = info[idx]+1
        sol(idx+1, cnt, score, target, arr + [0])
        if info[idx] == 0:
            sol(idx+1, cnt+1, score + num, target, arr + [1])
        else:
            sol(idx+1, cnt+t, score + num, target - num, arr + [t])
        
    
    # 어피치 점수 계산
    scores = 0
    for i in range(10):
        if info[i] > 0:
            scores += 10-i
            
    tmp = 0
    answer = []
    answer_min = 0
    sol(0, 0, 0, scores, [])
    
    if answer:
        return answer
    else:
        return [-1]