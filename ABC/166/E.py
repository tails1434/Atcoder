from collections import defaultdict

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    B = [0] * N
    for i in range(N):
        B[i] = (i + 1) - A[i]
        A[i] += i + 1

    d = defaultdict(int)
    ans = 0
    for i in range(N-1,0,-1):
        d[B[i]] += 1
        ans += d[A[i-1]]

    print(ans)

    


if __name__ == "__main__":
    main()