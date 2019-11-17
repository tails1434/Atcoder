def cmb(n, r, MOD, g1, g2):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % MOD


def main():
    X, Y = map(int, input().split())
    MOD = 10 ** 9 + 7
    if (X + Y) % 3 != 0:
        print(0)
        exit()
    m = (2 * X - Y) // 3
    n = (2 * Y - X) // 3

    
    N = 10**6
    g1 = [1, 1] # 元テーブル
    g2 = [1, 1] #逆元テーブル
    inverse = [0, 1] #逆元テーブル計算用テーブル
    
    for i in range( 2, N + 1 ):
        g1.append( ( g1[-1] * i ) % MOD )
        inverse.append( ( -inverse[MOD % i] * (MOD//i) ) % MOD )
        g2.append( (g2[-1] * inverse[-1]) % MOD )
    
    ans = cmb(n + m, n, MOD, g1, g2)
    print(ans)

if __name__ == "__main__":
    main()