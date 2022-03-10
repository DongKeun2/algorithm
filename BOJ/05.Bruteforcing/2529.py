# 부등호
# 백트래킹, 브루트포스

# 조건에 맞는 가장 큰 수 찾기
def sol1():
    global result1
    # tot1이 완성된 경우
    if len(tot1) >= k+1:
        # tot1이 결과보다 크다면 갱신
        if int(result1) < int(''.join(str(x) for x in tot1)):
            result1 = ''.join(str(x) for x in tot1)
            return
    else:
        for i in range(len(lst1)):
            # 아직 tot1에 포함되지 않은 수인 경우 
            if v[i] == 0:
                # tot1이 비었다면 넣어준다
                if tot1 == []:
                    v[i] = 1
                    tot1.append(lst1[i])
                    sol1()
                    v[i] = 0
                    tot1.pop()

                # 다음으로 들어가는 수인 lst1[i]이 조건에 부합하는지 확인
                elif bra[len(tot1)-1] == '<':
                    if tot1[-1] < lst1[i]:
                        v[i] = 1
                        tot1.append(lst1[i])
                        sol1()
                        v[i] = 0
                        tot1.pop()
                
                # 마찬가지
                else:
                    if tot1[-1] > lst1[i]:
                        v[i] = 1
                        tot1.append(lst1[i])
                        sol1()
                        v[i] = 0
                        tot1.pop()
        return

# 조건에 맞는 가장 작은 수 찾기
# sol1과 같은 구조
def sol2():
    global result2
    if len(tot2) >= k+1:
        if int(result2) > int(''.join(str(x) for x in tot2)):
            result2 = ''.join(str(x) for x in tot2)
            return
    else:
        for i in range(len(lst2)):
            if v[i] == 0:
                if tot2 == []:
                    v[i] = 1
                    tot2.append(lst2[i])
                    sol2()
                    v[i] = 0
                    tot2.pop()

                elif bra[len(tot2)-1] == '<':
                    if tot2[-1] < lst2[i]:
                        v[i] = 1
                        tot2.append(lst2[i])
                        sol2()
                        v[i] = 0
                        tot2.pop()
                
                else:
                    if tot2[-1] > lst2[i]:
                        v[i] = 1
                        tot2.append(lst2[i])
                        sol2()
                        v[i] = 0
                        tot2.pop()
        return

k = int(input())
bra = list(map(str, input().split()))

lst1 = [i for i in range(9-k, 10)]
tot1 = []
v = [0 for _ in range(k+1)]
result1 = '0'
sol1()
print(result1)

lst2 = [i for i in range(k+1)]
tot2 = []
v = [0 for _ in range(k+1)]
result2 = ''.join(str(x) for x in [n for n in range(k+1)[::-1]])
sol2()
print(result2)