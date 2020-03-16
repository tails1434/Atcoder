def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    pre = [''] * N
    ans = 0
    for i in range(N):
        if i - K < 0:
            if T[i] == 'r':
                ans += P
                pre[i] = 'p'
            if T[i] == 's':
                ans += R
                pre[i] = 'r'
            if T[i] == 'p':
                ans += S
                pre[i] = 's'
        else:
            if T[i] == 'r':
                if pre[i-K] == 'p':
                    continue
                ans += P
                pre[i] = 'p'
            if T[i] == 's':
                if pre[i-K] == 'r':
                    continue
                ans += R
                pre[i] = 'r'
            if T[i] == 'p':
                if pre[i-K] == 's':
                    continue
                ans += S
                pre[i] = 's'
    
    print(ans)

if __name__ == "__main__":
    main()