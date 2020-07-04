def main():
    N = int(input())
    X = []
    for _ in range(N):
        x, y = map(int,input().split())
        X.append([x,y])

    d = [[(0,0)] * N for _ in range(N)]
    b = set()
    for i in range(N):
        for j in range(N):
            d[i][j] = (X[i][0] - X[j][0], X[i][1] - X[j][1])
            if not (X[i][0] - X[j][0] == 0 and X[i][1] - X[j][1] == 0):
                b.add((X[i][0] - X[j][0], X[i][1] - X[j][1]))
    
    cnt = 0
    for a in b:
        tmp = 0
        for i in range(N):
            tmp += d[i].count(a)

        cnt = max(cnt, tmp)
    
    print(1 + (N - 1 - cnt))
            


if __name__ == "__main__":
    main()