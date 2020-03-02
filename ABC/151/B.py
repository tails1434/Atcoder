def main():
    N,K,M = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    ans = M * N - sum_A
    if ans > K:
        print(-1)
    else:
        print(max(ans,0))

if __name__ == "__main__":
    main()