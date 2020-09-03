def main():
    N, K = map(int, input().split())
    S = input()
    cnt = 0
    for i in range(1,N):
        if S[i] == S[i-1]:
            cnt += 1
    ans = min(N-1,cnt+2*K)
    print(ans)


if __name__ == "__main__":
    main()