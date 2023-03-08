# 쿼드압축 후 개수 세기 Lv2
# 월간 코드 챌린지 시즌1

def solution(arr):
    def sol(si, ei, sj, ej):
        s = arr[si][sj]
        for i in range(si, ei):
            for j in range(sj, ej):
                # 영역 중 다른 값이 존재한다면 4등분하여 다시 확인
                if arr[i][j] != s:
                    sol(si, (si+ei)//2, sj, (sj+ej)//2)
                    sol(si, (si+ei)//2, (sj+ej)//2, ej)
                    sol((si+ei)//2, ei, sj, (sj+ej)//2)
                    sol((si+ei)//2, ei, (sj+ej)//2, ej)
                    return
        # 모든 부분이 시작점과 같은 수라면 +1
        else:
            answer[s] += 1

    n = len(arr)
    answer = [0, 0]
    sol(0, n, 0, n)
    return answer