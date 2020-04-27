def main():
    N, K = map(int, input().split())
    MOD = 10 ** 9 + 7
    ans = 0
    cont = [0] * (K + 1)
    for i in range(K, 0, -1):
        tmp = K // i
        if tmp == 1:
            cont[i] = 1
        else:
            cont[i] = pow(tmp, N, MOD)
            for k in range(2,100005):
                if i * k > K:
                    break
                cont[i] -= cont[i*k]
                cont[i] %= MOD

    for i in range(1,K+1):
        ans += i * cont[i]
        ans %= MOD


    print(ans)


if __name__ == "__main__":
    main()