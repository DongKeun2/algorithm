# 2022 카카오 테크 인턴쉽
# lv2

def solution(queue1, queue2):
    n = len(queue1)
    m = len(queue2)
    s1 = sum(queue1)
    s2 = sum(queue2)
    
    # 합이 홀수라면 불가능
    if (s1 + s2) % 2:
        answer = -1
    else:
        m = (s1 + s2) // 2
        result = s1 - m
        
        q1 = queue1 + queue2
        q2 = queue2 + queue1
        
        # 연산 횟수 cnt, 두 리스트의 포인터 idx 
        cnt = 0
        idx1 = 0
        idx2 = 0
        answer = 0
        while True:
            # 같아지면 종료
            if result == 0:
                answer = cnt
                break

            # 큰 경우 q1에서 빼주고 포인터 이동
            if result > 0:
                if idx1 < len(q1):
                    result -= q1[idx1]
                    idx1 += 1
                else:
                    answer = -1
                    break
            # 작은 경우 q2에서 더해주고 포인터 이동
            else:
                if idx2 < len(q2):
                    result += q2[idx2]
                    idx2 += 1
                else:
                    answer = -1
                    break
            cnt += 1
    
    return answer