def main():
    x, y, W = input().split()
    C = [list(input()) for _ in range(9)]
    x = int(x) - 1 + 8
    y = int(y) - 1 + 8
    D = []
    for i in range(9):
        D.append(C[i][:0:-1] + C[i] + C[i][-2::-1])
    E = []
    for i in range(3):
        if i == 0:
            for j in range(8,0,-1):
                E.append(D[j])
        elif i == 1:
            for j in range(9):
                E.append(D[j])
        else:
            for j in range(7,-1,-1):
                E.append(D[j])
    if W == 'R':
        print(E[y][x]+E[y][x+1]+E[y][x+2]+E[y][x+3])
    elif W == 'L':
        print(E[y][x]+E[y][x-1]+E[y][x-2]+E[y][x-3])
    elif W == 'U':
        print(E[y][x]+E[y-1][x]+E[y-2][x]+E[y-3][x])
    elif W == 'D':
        print(E[y][x]+E[y+1][x]+E[y+2][x]+E[y+3][x])
    elif W == 'RU':
        print(E[y][x]+E[y-1][x+1]+E[y-2][x+2]+E[y-3][x+3])
    elif W == 'RD':
        print(E[y][x]+E[y+1][x+1]+E[y+2][x+2]+E[y+3][x+3])
    elif W == 'LU':
        print(E[y][x]+E[y-1][x-1]+E[y-2][x-2]+E[y-3][x-3])
    elif W == 'LD':
        print(E[y][x]+E[y+1][x-1]+E[y+2][x-2]+E[y+3][x-3])

if __name__ == "__main__":
    main()