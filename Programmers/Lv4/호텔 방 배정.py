import sys
sys.setrecursionlimit(10**6)

def solution(k, room_number):
    # dct에 키로 존재하지 않는 수는 아직 사용되지 않았다.
    # dct[x] = x로 사용 여부 표시
    # 만약 dct[x] = x라면 사용되었지만 갱신되지 않은 경우이므로 +1하여 다시 확인
    def check(x):
        if x in dct:
            if dct[x] == x:
                dct[x] = check(x+1)
            else:
                dct[x] = check(dct[x])
        else:
            dct[x] = x
            
        return dct[x]
    
    
    answer = []
    dct = {}
    for num in room_number:
        # dct에 있다면 가장 높은 수를 찾는다.
        if num in dct:
            dct[num] = check(dct[num])
            answer.append(dct[num])
        
        # dct에 없다면 그대로 추가
        else:
            answer.append(num)
            dct[num] = num+1
    return answer