# [1차] 추석 트래픽 Lv3
# 2018 KAKAO BLIND RECRUITMENT

# 모든 요청비교 (그리디)
## 요청마다 양 끝점을 기준으로 +- 1초 사이에 겹치는 요청 수 계산

# 문자열 분리하여 시간 계산
## ms단위 기준으로 시간을 정수로 변환
### 시작 시간과 끝 시간 nx, ny

# 시작점 기준 cnt1 cnt2 계산
## 끝점 기준 cnt3 cnt4 계산
### answer 갱신
def solution(lines):
    answer = 1
    n = len(lines)
    for i in range(n):
        nl = lines[i].split()
        nt, nc = nl[1], nl[2][:-1]
        nh, nm, ns = nt.split(':')
        ny = int(nh) * 60 * 60000 + int(nm) * 60000 + float(ns) * 1000
        nx = ny - float(nc) * 1000 + 1
        
        cnt1 = 1
        cnt2 = 1
        cnt3 = 1
        cnt4 = 1
        for j in range(n):
            if i != j:
                ml = lines[j].split()
                mt, mc = ml[1], ml[2][:-1]
                mh, mm, ms = mt.split(':')
                my = int(mh) * 60 * 60000 + int(mm) * 60000  + float(ms) * 1000
                mx = my - float(mc) * 1000 + 1
                if nx <= mx < nx+1000 or nx <= my < nx+1000 or (mx <= nx and nx+1000 <= my):
                    cnt1 += 1
                if nx-1000 < mx <= nx or nx-1000 < my <= nx or (mx <= nx-1000 and nx <= my):
                    cnt2 += 1
                if ny <= mx < ny+1000 or ny <= my < ny+1000 or (mx <= ny and ny+1000 <= my):
                    cnt3 += 1
                if ny-1000 < mx <= ny or ny-1000 < my <= ny or (mx <= ny-1000 and ny <= my):
                    cnt4 += 1
        answer = max(cnt1, cnt2, cnt3, cnt4, answer)
    return answer