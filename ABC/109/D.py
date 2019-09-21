def main():
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))

    ope = []

    for i in range(H-1):
        for j in range(W):
            if A[i][j] % 2 == 1:
                A[i][j] -= 1
                A[i+1][j] += 1
                ope.append([i+1,j+1,i+2,j+1])
    for j in range(W-1):
        if A[H-1][j] % 2 == 1:
            A[H-1][j] -= 1
            A[H-1][j+1] += 1
            ope.append([H,j+1,H,j+2])
            

    print(len(ope))
    for o in ope:
        print(*o) 

main()