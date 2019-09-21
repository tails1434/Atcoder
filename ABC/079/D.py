def war(d,N):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j],d[i][k]+d[k][j])
    return d



def main():
    H, W = map(int, input().split())

    c = [list(map(int, input().split())) for i in range(10)]

    c = war(c,10)

    A = [list(map(int, input().split())) for i in range(H)]
    ans = 0

    for i in range(H):
        for j in range(W):
            if A[i][j] == -1 or A[i][j] == 1:
                continue
            else:
                ans += c[A[i][j]][1]

    print(ans)


main()