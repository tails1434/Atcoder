from itertools import accumulate

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = 0
    E = [0] * N
    for i in range(N):
        E[i] = ((P[i] * (P[i] + 1)) // 2) / P[i]

    F = [0] + list(accumulate(E))
    ans = 0
    for i in range(N-K+1):
        tmp = F[i+K] - F[i]
        ans = max(ans, tmp)

    print(ans)






if __name__ == "__main__":
    main()