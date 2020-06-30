def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = A[0]
    for i in range(1,N):
        B ^= A[i]

    ans = [0] * N
    for i in range(N):
        ans[i] = B ^ A[i]

    print(*ans)

if __name__ == "__main__":
    main()