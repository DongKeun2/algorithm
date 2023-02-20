# 2021 카카오 블라인드 Lv3

# 총 시간 lst에 광고 수 누적합
def solution(play_time, adv_time, logs):
    h, m, s = map(int, play_time.split(':'))
    tt = h*3600 + m*60 + s
    ph, pm, ps = map(int, adv_time.split(':'))
    pt = ph*3600 + pm*60 + ps

    # 시작시간 리스트 stl 생성 및 추가
    lst = [0] * (tt+2)
    stl = set()
    stl.add(0)
    stl.add(tt-pt)
    for log in logs:
        sl = log.split('-')
        sh, sm, ss = map(int, sl[0].split(':'))
        eh, em, es = map(int, sl[1].split(':'))
        st = sh*3600 + sm*60 + ss
        et = eh*3600 + em*60 + es
        stl.add(st)
        stl.add(et-pt)
        lst[st+1] += 1
        lst[et+1] -= 1
    
    # 광고 수 누적합
    for t in range(1, tt+2):
        lst[t] += lst[t-1]
    for t in range(1, tt+2):
        lst[t] += lst[t-1]
    
    # 시작시간 st 기준으로 광고 수 비교 및 갱신
    cnt = 0
    result = 0
    for st in stl:
        if st + pt <= tt:
            num = lst[st+pt] - lst[st]
            if num == cnt and result > st:
                result = st
            elif num > cnt:
                cnt = num
                result = st
    
    # 결과 형식에 맞게 출력 
    rh = '0' + str(result // 3600) if len(str(result // 3600)) == 1 else str(result // 3600)
    rm = '0' + str((result % 3600) // 60) if len(str((result % 3600) // 60)) == 1 else str((result % 3600) // 60)
    rs = '0' + str(result % 60) if len(str(result % 60)) == 1 else str(result % 60)
    answer = '{}:{}:{}'.format(rh,rm,rs)
    return answer