from math import gcd

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    S = list(map(int, input().split()))
    for i in range(1,N):
        A[i] = gcd(A[i], A[i-1])

    for i in range(Q):
        X = S[i]
        t = gcd(A[-1], X)
        if t != 1:
            print(t)
        else:
            ng = -1
            ok = N - 1
            while ok - ng > 1:
                mid = (ok + ng) // 2
                if gcd(X, A[mid]) == 1:
                    ok = mid
                else:
                    ng = mid

            print(ok + 1)



if __name__ == "__main__":
    main()