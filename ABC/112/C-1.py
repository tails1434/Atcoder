def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    H = [0] * N
    for i in range(N):
        X[i], Y[i], H[i] = map(int, input().split())
    ans = []
    for x in range(101):
        for y in range(101):
            tmp = 0
            for i in range(N):
                if H[i] == 0:
                    continue
                else:
                    tmp = H[i] + abs(X[i] - x) + abs(Y[i] - y)
                    break
            for i in range(N):
                if not (H[i] == max(tmp - abs(X[i] - x) - abs(Y[i] - y),0)):
                    break
            else:
                ans = [x,y,tmp]
                break
    if N == 1:
        if H[0] == 0:
            print(X[0],Y[0],H[0])
            exit()
    print(*ans)
            



if __name__ == "__main__":
    main()