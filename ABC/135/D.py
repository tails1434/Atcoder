# python3だとTLEだったので色々いじっていたが、pypy3だと通ってしまった・・・
def main():
    S = list(input())

    dp = [0] * 13
    dp[0] = 1
    mod = 10**9 + 7
    digit = 1
    for i in range(len(S)-1,-1,-1):
        nextdp = [0] * 13
        if S[i] == '?':
            for j in range(10):
                for k in range(13):
                    nextdp[(j * digit + k) % 13] += dp[k]
                    # あらかじめ10*9 + 7で割って余りを出しておく
                    nextdp[(j * digit + k) % 13] %= mod
        else:
            j = int(S[i])
            for k in range(13):
                nextdp[(j * digit + k) % 13] += dp[k]
                # あらかじめ10*9 + 7で割って余りを出しておく
                nextdp[(j * digit + k) % 13] %= mod
        
        digit *= 10
        # A * 桁数の13で割ったあまりは (A % 13) * (桁数 % 13)のため、桁数を13で割っておく
        digit %= 13
        dp = nextdp
    
    print(dp[5])

main()