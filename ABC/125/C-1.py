from math import gcd

def main():
    N = int(input())
    A = list(map(int, input().split()))
    R = [0] * (N+1)
    L = [0] * (N+1)
    for i in range(N):
        L[i+1] = gcd(L[i], A[i])

    for i in range(N-1,-1,-1):
        R[i] = gcd(R[i+1], A[i])
    ans = 0
    for i in range(N):
        ans = max(ans, gcd(L[i],R[i+1]))
    print(ans)

if __name__ == "__main__":
    main()