# 암호 만들기
# 수학, 브루트포스, 조합론, 백트래킹

def sol():
    # 조건에 맞게 L만큼 result를 채운다면 출력
    if len(result) >= L:
        print(''.join(str(x) for x in result))
        return
    
    # 아직이라면 조건을 비교하며 result에 추가하는 작업
    else:
        # 입력받은 lst를 돌면서 자음, 모음 경우 나누어 생각
        for i in range(C):

            # 모음인 경우
            if v[i] == 0 and lst[i] in vow:
                cnt = 0
                for j in range(len(result)):
                    if result[j] in vow:
                        cnt += 1
                # 자음 2개 이상이 들어갈 자리는 만들어 놓고 추가
                if cnt < L-2:
                    if result and result[-1] < lst[i]:
                        v[i] = 1
                        result.append(lst[i])
                        sol()
                        result.pop()
                        v[i] = 0
                    elif result == []:
                        v[i] = 1
                        result.append(lst[i])
                        sol()
                        result.pop()
                        v[i] = 0
            
            # 자음인 경우
            elif v[i] == 0:
                # result안에 자음이 1개 이상있다면 사전순 배열만 생각하여 추가
                for j in range(len(result)):
                    if result[j] in vow:
                        if result and result[-1] < lst[i]:
                            v[i] = 1
                            result.append(lst[i])
                            sol()
                            result.pop()
                            v[i] = 0
                        break
                # result안에 자음이 없다면 자음이 들어갈 자리는 남겨두고 추가
                else:
                    if len(result) < L-1:
                        if result and result[-1] < lst[i]:
                            v[i] = 1
                            result.append(lst[i])
                            sol()
                            result.pop()
                            v[i] = 0
                        elif result == []:
                            v[i] = 1
                            result.append(lst[i])
                            sol()
                            result.pop()
                            v[i] = 0
        return

L, C = map(int, input().split())
lst = list(map(str, input().split()))
v = [0 for _ in range(C)]
vow = ['a', 'e', 'i', 'o', 'u']
lst.sort()
result = []
sol()