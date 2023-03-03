# 이모티콘 할인행사 Lv2
# 2023 KAKAO BLIND RECRUITMENT

from itertools import product

def solution(users, emoticons):
    global answer
    def sol(tmp):
        global answer
        arr = [0, 0]
        for p, m in users:
            t = 0
            for i in range(n):
                if tmp[i] >= p:
                    t += emoticons[i] * (100-tmp[i]) / 100
            if t >= m:
                arr[0] += 1
            else:
                arr[1] += t
        if answer[0] < arr[0]:
            answer = arr
        elif answer[0] == arr[0] and answer[1] < arr[1]:
            answer = arr
            
    
    # 이모티콘마다 10, 20, 30, 40 할인율로 계산
    # 유저의 구매비용과 가입여부 확인
    answer = [0, 0]
    n = len(emoticons)
    d = [10, 20, 30, 40]
    for lst in product(d, repeat=n):
        sol(lst)

    return answer