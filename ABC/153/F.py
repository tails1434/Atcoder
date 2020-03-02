from bisect import bisect_right
import sys
input = sys.stdin.readline

def main():
    N, D, A = map(int, input().split())
    B = []

    for i in range(N):
        x, h = map(int, input().split())
        B.append((x,h))

    B.sort()
    X = [0] * N
    H = [0] * N
    for i in range(N):
        X[i], H[i] = B[i]
    ans = 0
    ok = [False] * N
    S = [0] * (N + 1)
    for i in range(N):
        if S[i] < H[i]:
            cnt = (H[i] - S[i]) // A if (H[i] - S[i]) % A == 0 else (H[i] - S[i]) // A + 1
            ans += cnt
            search_max = bisect_right(X, X[i] + 2 * D)
            S[i] += cnt * A
            S[search_max] -= cnt * A
        
        S[i+1] += S[i]

    print(ans)



if __name__ == "__main__":
    main()