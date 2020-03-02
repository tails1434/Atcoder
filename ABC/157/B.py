from collections import defaultdict

def main():
    A = [list(map(int, input().split())) for _ in range(3)]
    d = defaultdict(list)

    for i in range(3):
        for j in range(3):
            d[A[i][j]].append(i)
            d[A[i][j]].append(j)

    bingo = [[False] * 3 for _ in range(3)]
    N = int(input())
    for _ in range(N):
        b = int(input())
        if d[b]:
            i, j = d[b]
            bingo[i][j] = True

    for i in range(3):
        flag = True
        for j in range(3):
            if bingo[i][j] == False:
                flag = False
                break
        if flag:
            print('Yes')
            exit()

    for j in range(3):
        flag = True
        for i in range(3):
            if bingo[i][j] == False:
                flag = False
                break
        if flag:
            print('Yes')
            exit()
    
    if bingo[0][0] == True and bingo[1][1] == True and bingo[2][2] == True:
        print('Yes')
        exit()

    if bingo[2][0] == True and bingo[1][1] == True and bingo[0][2] == True:
        print('Yes')
        exit()

    print('No')
if __name__ == "__main__":
    main()