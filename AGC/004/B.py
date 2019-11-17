def main():
    N, x = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    ans = float('inf')
    for k in range(N):
        can = k * x
        for i in range(N):
            if k == 0:
                B[i] = A[i]
            else:
                B[i] = min(B[i],A[i-k])
            can += B[i]
        ans = min(ans, can)

    print(ans)
    

if __name__ == "__main__":
    main()