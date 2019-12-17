from itertools import accumulate

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] + list(accumulate(A))
    ans = 0
    MOD = 10 ** 9 + 7
    print(B)
    for i in range(N-1):
        print(A[i], B[N] - B[i])
        ans += A[i] ^ (B[N] - B[i-1])
        ans %= MOD

    print(ans)



if __name__ == "__main__":
    main()