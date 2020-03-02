def main():
    N = int(input())
    cnt = 0
    '''
    i => Aの末尾の桁が Bの先頭の桁
    j => Bの末尾の桁が Aの先頭の桁
    '''
    cnt = [[0] * 10 for _ in range(10)]
    for i in range(N+1):
        tmp = str(i)
        first = int(tmp[0])
        last = int(tmp[-1])
        cnt[first][last] += 1
    ans = 0
    for i in range(1,10):
        for j in range(1,10):
            ans += cnt[i][j] * cnt[j][i]

    print(ans)

        







if __name__ == "__main__":
    main()