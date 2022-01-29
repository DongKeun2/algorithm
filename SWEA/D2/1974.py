# 스도쿠 검증


def kkkk(n_list):

    for j in range(9):
        n_set = set()
        for k in range(9):
            n_set.add(n_list[j][k])
        if len(n_set) < 9:
            return 0
    
    for j in range(9):
        n_set = set()
        for k in range(9):
            n_set.add(n_list[k][j])
        if len(n_set) < 9:
            return 0

    for j in range(3):
        for m in range(3):
            n_set = set()
            for k in range(3*j, 3*j +3):
                for l in range(3*m, 3*m + 3):
                    n_set.add(n_list[k][l])
            if len(n_set) < 9:
                return 0
                
    return 1


T = int(input())

for i in range(1, T+1):
    n_list = []
    for _ in range(9):
        n_list.append(list(map(int, input().split())))

    print(f'#{i}', kkkk(n_list))
