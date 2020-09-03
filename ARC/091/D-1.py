def main():
    N, K = map(int, input().split())
    ans = 0
    
    for i in range(K+1,N+1):
        cnt = i - K
        cnt *= N // i
        cnt += max((N % i) - K + 1,0)
        ans += cnt
    if K == 0:
        ans -= N
    print(ans)


if __name__ == "__main__":
    main()