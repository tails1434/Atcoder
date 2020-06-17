
def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for _ in range(K):
        B = [0] * (N + 1)
        for i in range(N):
            l = max(0,i-A[i])
            r = min(N,i+A[i]+1)
            B[l] += 1
            B[r] -= 1
        for i in range(N):
            B[i+1] += B[i]
        B.pop(-1)
        if A == B:
            break
        A = B

    print(*A)
    

if __name__ == "__main__":
    main()