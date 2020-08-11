from bisect import bisect_left

def main():
    N, M = map(int, input().split())
    P = [0] + [int(input()) for _ in range(N)]
    P.sort()
    A = []
    for i in range(N+1):
        for j in range(N+1):
            if P[i] + P[j] <= M:
                A.append(P[i]+P[j])
    A.sort()
    ans = 0
    for a in A:
        index = max(0,bisect_left(A, M-a) - 1)
        if a+A[index] <= M:
            ans = max(ans, a+A[index])

    print(ans)

if __name__ == "__main__":
    main()