# 빙고

xl = []
yl = []
for _ in range(5):
    xl.append(list(map(int, input().split())))
for _ in range(5):
    yl.append(list(map(int, input().split())))

cnt = 0
b = 0
result = 0
for i in range(5):
    if b == 3:
        break
    for j in range(5):
        if b == 3:
            break
        for m in range(5):
            if b == 3:
                break
            for n in range(5):
                if yl[i][j] == xl[m][n]:
                    xl[m][n] = 0
                    cnt += 1
                    if sum(xl[m]) == 0:
                        b += 1
                        if b == 3:
                            result = cnt
                            break
                    if m == n:
                        for k in range(5):
                            if xl[k][k] != 0:
                                break
                        else:
                            b += 1
                            if b == 3:
                                result = cnt
                                break
                    if m+n == 4:
                        for r in range(5):
                            if xl[r][4-r] != 0:
                                break
                        else:
                            b += 1
                            if b == 3:
                                result = cnt
                                break
                    for k in xl:
                        if k[n] != 0:
                            break
                    else:
                        b += 1
                        if b == 3:
                            result = cnt
                            break
            
print(result)