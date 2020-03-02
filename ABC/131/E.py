def main():
    N, K = map(int, input().split())
    mx = (N - 1) * (N - 2) // 2
    if mx < K:
        print(-1)
        exit()
    ans = []

    for i in range(2,N+1):
        ans.append((1,i))

    cnt = mx - K
    for j in range(2, N+1):
        for k in range(j,N+1):
            if cnt == 0:
                break
            if j == k:
                continue
            ans.append((j,k))
            cnt -= 1

    print(len(ans))
    for a,b in ans:
        print(a,b)
    



    



if __name__ == "__main__":
    main()