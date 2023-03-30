# 과제 진행하기 Lv2
# 연습문제

# 스택 활용 풀이
# 스택에 과제명, 남은 시간 저장
# 다음 과제 시작 시간과 비교하며 풀이가 가능한지 여부 판별
def solution(plans):
    answer = []
    arr = []
    for plan in plans:
        name = plan[0]
        h, m = map(int, plan[1].split(':'))
        t = int(plan[2])
        arr.append((name, h*60 + m, t))
    
    arr.sort(key= lambda x : x[1])
    st = []
    for i in range(len(arr)-1):
        n, s, t = arr[i]
        if s + t <= arr[i+1][1]:
            answer.append(n)
            tot = arr[i+1][1] - s - t
            while st:
                name, time = st.pop()
                if tot >= time:
                    tot -= time
                    answer.append(name)
                else:
                    st.append((name, time - tot))
                    break
                
        else:
            st.append((n, t - (arr[i+1][1] - s)))
    answer.append(arr[-1][0])
    
    while st:
        answer.append(st.pop()[0])
    return answer