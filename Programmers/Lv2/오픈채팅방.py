# 오픈채팅방 Lv2
# 2019 KAKAO BLIND RECRUITMENT

def solution(record):
    dct = {}
    for S in record:
        lst = S.split()
        if lst[0] != 'Leave':
            t, user, name = S.strip().split()
            dct[user] = name
    
    answer = []
    for S in record:
        lst = S.split()
        if len(lst) <= 2:
            t, user = S.strip().split()
            answer.append('{}님이 나갔습니다.'.format(dct[user]))
        else:
            t, user, x = S.strip().split()
            if t == 'Enter':
                answer.append('{}님이 들어왔습니다.'.format(dct[user]))
    
    return answer