def main():
    N = int(input())
    a = list(map(int,list(input())))
    dp = [[[0] * 4 for _ in range(4)] for _ in range(4)]

    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                tmp = abs(abs(i-j) - abs(j-k))
                dp[i][j][k] = tmp
    ans = 0
    print(dp)
    for i in range(1,N-1):
        ans = abs(ans - dp[a[i-1]][a[i]][a[i+1]])
    print(ans)





if __name__ == "__main__":
    main()