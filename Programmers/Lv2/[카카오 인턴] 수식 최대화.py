# [카카오 인턴] 수식 최대화
# 2020 카카오 인턴십

# 스택 활용 풀이
# 모든 경우의 수를 계산
import copy
from itertools import permutations

def solution(expression):
    def sol(op):
        exp = copy.deepcopy(lst)
        idx = 0
        while idx < 3:
            tmp = []
            flag = False
            if op[idx] == 0:
                for i in range(len(exp)):
                    if flag:
                        flag = False
                    elif exp[i] == '+':
                        tmp.append(int(tmp.pop()) + int(exp[i+1]))
                        flag = True
                    else:
                        tmp.append(exp[i])
                        
            elif op[idx] == 1:
                for i in range(len(exp)):
                    if flag:
                        flag = False
                    elif exp[i] == '-':
                        tmp.append(int(tmp.pop()) - int(exp[i+1]))
                        flag = True
                    else:
                        tmp.append(exp[i])
            else:
                for i in range(len(exp)):
                    if flag:
                        flag = False
                    elif exp[i] == '*':
                        tmp.append(int(tmp.pop()) * int(exp[i+1]))
                        flag = True
                    else:
                        tmp.append(exp[i])
            exp = copy.deepcopy(tmp)
            idx += 1
        return abs(exp[0])
    
    
    answer = 0
    lst = []
    x = ''
    for s in expression:
        if s == '+' or s == '-' or s == '*':
            lst.append(x)
            lst.append(s)
            x = ''
        else:
            x += s
    lst.append(x)
    
    for arr in permutations((0,1,2), 3):
        answer = max(answer, sol(arr))
    return answer