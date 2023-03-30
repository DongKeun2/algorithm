# 행렬 테두리 회전하기 Lv2
# 2021 Dev-Matching: 웹 백엔드 개발자(상반기)

# 모서리 부분 값을 저장한 뒤 회전
import sys
sys.setrecursionlimit(10**6)

def solution(rows, columns, queries):
    def sol(idx):
        if idx >= n:
            return
        si, sj, ei, ej = queries[idx]
        si -= 1
        sj -= 1
        ei -= 1
        ej -= 1
        
        sisj = arr[si+1][sj]
        siej = arr[si][ej-1]
        eisj = arr[ei][sj+1]
        eiej = arr[ei-1][ej]
        cnt = min(sisj, siej, eisj, eiej)
        
        for i in range(si+1, ei)[::-1]:
            arr[i][ej] = arr[i-1][ej]
            cnt = min(cnt, arr[i][ej])
        
        for i in range(si+1, ei):
            arr[i][sj] = arr[i+1][sj]
            cnt = min(cnt, arr[i][sj])
            
        for j in range(sj+1, ej)[::-1]:
            arr[si][j] = arr[si][j-1]
            cnt = min(cnt, arr[si][j])
            
        for j in range(sj+1, ej):
            arr[ei][j] = arr[ei][j+1]
            cnt = min(cnt, arr[ei][j])
        
        arr[si][sj] = sisj
        arr[si][ej] = siej
        arr[ei][sj] = eisj
        arr[ei][ej] = eiej
        
        answer.append(cnt)
        sol(idx+1)
        return
    
    n = len(queries)
    arr = [[(j+1)+(i*columns) for j in range(columns)] for i in range(rows)]
    answer = []
    sol(0)
    
    return answer