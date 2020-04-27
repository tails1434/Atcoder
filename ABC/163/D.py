from itertools import accumulate

def main():
    N, K = map(int, input().split())
    MOD = 10 ** 9 + 7
    A = list(range(0,N+1))
    B = list(accumulate(A))
    A.reverse()
    C = list(accumulate(A))
    ans = 0
    for r in range(K, N+2):
        r -= 1
        t_max = C[r]
        t_min = B[r]
        ans += t_max - t_min + 1 
        ans %= MOD
    print(ans)





if __name__ == "__main__":
    main()