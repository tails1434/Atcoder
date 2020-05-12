from collections import defaultdict

def main():
    N, K = map(int, input().split())
    d = [0] * K
    A = [[] for _ in range(K)]
    B = defaultdict(int)
    for i in range(K):
        d[i] = int(input())
        A[i] = list(map(int, input().split()))
        for a in A[i]:
            B[a] += 1
    ans = 0
    for i in range(1,N+1):
        if B[i] == 0:
            ans += 1
    print(ans)



if __name__ == "__main__":
    main()