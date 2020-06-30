def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    ans = 1
    cnt = [0] * (N + 1)
    for i in range(N):
        if A[i] == 0:
            ans *= 3 - cnt[A[i]]
            cnt[A[i]] += 1
        else:
            ans *= cnt[A[i]-1] - cnt[A[i]]
            cnt[A[i]] += 1
        ans %= MOD

    print(ans)

    



if __name__ == "__main__":
    main()