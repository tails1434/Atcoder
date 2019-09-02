from collections import defaultdict

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    A2 = A + A
    d2 = defaultdict(int)
    for i in range(2*N):
        for j in range(i,2*N):
            if A2[i] > A2[j]:
                d2[A2[i]] += 1

    d = defaultdict(int)
    for i in range(N):
        for j in range(i,N):
            if A[i] > A[j]:
                d2[A2[i]] -= 1
                d[A[i]] += 1
    ans = 0

    for key,value in d2.items():
        ans += (K * ((2 * d[key] + (K - 1) * (value - d[key])))) // 2
        
    print(int(ans) % MOD)

main()