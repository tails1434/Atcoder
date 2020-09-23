def main():
    N = int(input())
    cand = [1]
    dp = [float('inf')] * (N + 5)
    tmp = 6
    cnt = 1
    while tmp**cnt <= N:
        cand.append(tmp**cnt)
        cnt += 1
    tmp = 9
    cnt = 1
    while tmp**cnt <= N:
        cand.append(tmp**cnt)
        cnt += 1
    cand.sort()
    dp[0] = 0
    for i in range(N+1):
        for c in cand:
            if i + c <= N:
                dp[i+c] = min(dp[i+c], dp[i] + 1)
    print(dp[N])

if __name__ == "__main__":
    main()