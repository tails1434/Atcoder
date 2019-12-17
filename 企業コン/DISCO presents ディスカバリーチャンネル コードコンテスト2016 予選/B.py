import math

def main():
    R, N, M = map(int, input().split())
    def calc(n):
        if n <= 0 or N <= n:
            return 0
        if n > N / 2:
            return calc(N - n)
        t = R - (2 * R * n / N)
        return math.sqrt(R * R - t * t)*2
    ans = 0
    for i in range(1, N + M):
        ans += max(calc(i), calc(i-M))

    print(ans)

if __name__ == "__main__":
    main()