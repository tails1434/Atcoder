from itertools import accumulate

def main():
    N, K = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    B = [0] * N
    for i in range(N-1):
        if A[i] < A[i+1]:
            B[i] = 1
    C = [0] + list(accumulate(B))
    ans = 0
    for i in range(1,N-K+2):
        if C[i+K-2] - C[i-1] == K-1:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()