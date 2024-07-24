# AC, 골드5

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    fn = input().strip()
    n = int(input())
    tmp = input().strip()
    lst = list(map(int, tmp.lstrip('[').rstrip(']').split(','))) if not tmp == '[]' else []
    
    flag = True # 정방향
    error = False # []인데 D인 경우
    for s in fn:
        if s == 'R': flag = not flag
        else:
            if lst:
                if flag: lst.pop(0)
                else: lst.pop()
            else:
                error = True

    answer = 'error' if error else str(lst) if flag else str(list(reversed(lst))) 
    print(answer.replace(' ', ''))