# [3차] 방금그곡 Lv2
# 2018 KAKAO BLIND RECRUITMENT

def solution(m, musicinfos):
    answer = ''
    arr = []
    for k, lst in enumerate(musicinfos):
        st, et, title, tmp = lst.split(',')
        n = len(tmp)
        sh, sm = st.split(':')
        eh, em = et.split(':')
        time = (int(eh)-int(sh))*60 + (int(em)-int(sm))

        idx = 0
        play = []
        t = time
        while t > idx:
            if tmp[idx%n] == '#':
                t += 1
                play[-1] += '#'
            else:
                play.append(tmp[idx%n])
            idx += 1
            
        if tmp[idx%n] == '#':
            play[-1] += '#'
        
        X = m.split('#')
        l = 0
        for x in X:
            l += len(x)
        
        for i in range(len(play)-l+1):
            if m == ''.join(play[i:i+l]):
                arr.append([title, time, k])
                break

    if arr:
        arr.sort(key = lambda x : (-x[1], x[2]))
        answer = arr[0][0]
    else:
        answer = '(None)'
    return answer