# [1차] 다트 게임 Lv1
#  2018 KAKAO BLIND RECRUITMENT

# 3번의 기회를 문자열로 lst에 담기
# lst를 돌면서 조건에 맞게 answer을 갱신
# answer의 합을 반환

def solution(dartResult):
    # 한 번의 기회 당 최소 2이상의 문자열이므로
    # ord함수로 숫자를 찾고 길이가 2 이상일 때 잘라준다.
    lst = []
    tmp = ''
    for s in dartResult:
        if len(tmp) > 1 and 48 <= ord(s) <= 57:
            lst.append(tmp)
            tmp = ''
        tmp += s
    lst.append(tmp)
    
    # 각 기회별로 앞에서부터 몇 점인지 확인
    # 옵션은 마지막에 있으므로 -1번 인덱스가 옵션인지 확인
    answer = [0, 0, 0]
    for i in range(3):
        s = lst[i]
        num = ''
        for x in s:
            if 48 <= ord(x) <= 57:
                num += x
            else:
                break
                
        if s[len(num)] == 'S':
            answer[i] += int(num)
        elif s[len(num)] == 'D':
            answer[i] += int(num) ** 2
        else:
            answer[i] += int(num) ** 3
            
        
        if s[-1] == '#':
            answer[i] = -answer[i]
        elif s[-1] == '*':
            answer[i] *= 2
            if i > 0:
                answer[i-1] *= 2
        
    answer = sum(answer)
    return answer